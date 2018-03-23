""" ModelSettings
"""
import configparser
from distutils.util import strtobool
import inspect
import json
import logging
import os
import sys

from argparse import ArgumentParser, RawTextHelpFormatter
from envparse import env, ConfigurationError
import yaml



class ModelSettings(object):
    """ The ModelSettings class
    """
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.cwd = os.getcwd()

        settings_file = os.environ.get("MODEL_SETTINGS",
                                       f"{self.cwd}/model_settings.yml")
        try:
            with open(settings_file, 'r') as stream:
                filec = yaml.load(stream)
        except FileNotFoundError as _err:
            self.log.critical(f"Error finding {settings_file}")
            sys.exit(1)
        except yaml.YAMLError as _err: #pragma: no cover
            self.log.critical(f"Error parsing {settings_file}")
            sys.exit(1)

        try:
            self.spec = filec['model']
            for _key, value in filec['model'].items():
                value['type'] = type(value['example'])
        except KeyError:  #pragma: no cover
            self.log.critical(f"Missing 'model' key in {settings_file}")
            sys.exit(1)

        try:
            self.env_prefix = filec['env_prefix']
        except KeyError:  #pragma: no cover
            self.log.critical(f"Missing 'env_prefix' key in {settings_file}")
            sys.exit(1)

        self.set_defaults()
        args = self.parse_args()
        self.load_ini(ini_file=args.settings)
        self.load_env()
        self.add_args(args)
        if getattr(self, 'GENERATE', None):
            self.generate()
        else:
            self.check_required()

    @staticmethod
    def help(setting):
        """ Format the help string for argparse

            Args:
                setting (dict): One setting dict

        """
        example = f"e.g., {setting['example']}"
        return " ".join(filter(None, (setting.get('help'), example)))

    def set_defaults(self):
        """ Add each model entry with it's default
        """
        for key, value in self.spec.items():
            setattr(self, key.upper(), value.get("default", None))

    def load_env(self):
        """ Load the model fron environment variables
        """
        for key, value in self.spec.items():
            if value['type'] in (dict, list):
                envar = (self.env_prefix + "_" + key).upper()
                try:
                    envvar = env.json(envar,
                                      default=getattr(self, key.upper(), value.get('default')))
                except ConfigurationError as _err:  #pragma: no cover
                    print(_err)
                    self.log.critical(f"Error parsing json from env var. {os.environ.get(envar)}")
                    print(envar)
                    raise
            else:
                envvar = env((self.env_prefix + "_" + key).upper(),
                             default=getattr(self, key.upper(), value.get('default')),
                             cast=value['type'])
            setattr(self, key.upper(), envvar)


    def parse_args(self):
        """ Parse the cli args

            Returns:
                args (namespace): The args
        """
        parser = ArgumentParser(description='',
                                formatter_class=RawTextHelpFormatter)
        parser.add_argument("--generate", action="store", dest='generate',
                            choices=['command', 'docker-run', 'docker-compose',
                                     'ini', 'env', 'kubernetes', 'readme', 'drone-plugin'],
                            help="Generate a template ")
        parser.add_argument("--settings", action="store", dest='settings',
                            help="Specify a settings file. (ie settings.dev)")
        for key, value in self.spec.items():
            if value['type'] in [str, int, float]:
                parser.add_argument(f"--{key.lower()}", action="store", dest=key,
                                    type=value['type'],
                                    choices=value.get("choices"),
                                    help=self.help(value))
            elif value['type'] == bool:
                parser.add_argument(f"--{key.lower()}", action="store", dest=key,
                                    type=lambda x:bool(strtobool(x)),
                                    choices=value.get("choices"),
                                    help=self.help(value))
            elif value['type'] == list:
                parser.add_argument(f"--{key.lower()}", action="store", dest=key,
                                    nargs='+',
                                    choices=value.get("choices"),
                                    help=self.help(value))
            elif value['type'] == dict:
                parser.add_argument(f"--{key.lower()}", action="store", dest=key,
                                    type=json.loads,
                                    choices=value.get("choices"),
                                    help=self.help(value))
        args, _unknown = parser.parse_known_args()
        return args

    def add_args(self, args):
        """ Add the args

            Args:
                args (namespace): The commandline args

        """
        for key, value in vars(args).items():
            if value is not None:
                setattr(self, key.upper(), value)

    def load_ini(self, ini_file):
        """ Load the contents from the ini file

            Args:
                ini_file (str): The file from which the settings should be loaded

        """
        if ini_file and not os.path.exists(ini_file):
            self.log.critical(f"Settings file specified but not found. {ini_file}")
            sys.exit(1)
        if not ini_file:
            ini_file = f"{self.cwd}/settings.ini"
        if os.path.exists(ini_file):
            config = configparser.RawConfigParser(allow_no_value=True)
            config.read(ini_file)
            for key, value in self.spec.items():
                entry = None
                if value['type'] == str:
                    entry = config.get("settings", option=key.lower(), fallback=None)
                elif value['type'] == bool:
                    entry = config.getboolean("settings", option=key.lower(), fallback=None)
                elif value['type'] == int:
                    entry = config.getint("settings", option=key.lower(), fallback=None)
                elif value['type'] == float:
                    entry = config.getfloat("settings", option=key.lower(), fallback=None)
                elif value['type'] in [list, dict]:
                    entries = config.get("settings", option=key.lower(), fallback=None)
                    if entries:
                        try:
                            entry = json.loads(entries)
                        except json.decoder.JSONDecodeError as _err:  #pragma: no cover
                            self.log.critical(f"Error parsing json from ini file. {entries}")
                            sys.exit(1)
                if entry is not None:
                    setattr(self, key.upper(), entry)

    def check_required(self):
        """ Check all required settings have been provided
        """
        die = False
        for key, value in self.spec.items():
            if not getattr(self, key.upper()) and value['required']:
                print(f"{key} is a required setting. "
                      "Set via command-line params, env or file. "
                      "For examples, try '--generate' or '--help'.")
                die = True
        if die:
            sys.exit(1)

    def generate(self):
        """ Generate sample settings
        """
        otype = getattr(self, 'GENERATE')
        if otype:
            if otype == 'env':
                self.generate_env()
            elif otype == "command":
                self.generate_command()
            elif otype == "docker-run":
                self.generate_docker_run()
            elif otype == "docker-compose":
                self.generate_docker_compose()
            elif otype == "kubernetes":
                self.generate_kubernetes()
            elif otype == 'ini':
                self.generate_ini()
            elif otype == 'readme':
                self.generate_readme()
            elif otype == 'drone-plugin':
                self.generate_drone_plugin()

        sys.exit(0)


    def generate_env(self):
        """ Generate sample environment variables
        """
        for key in sorted(list(self.spec.keys())):
            if self.spec[key]['type'] in (dict, list):
                value = f"\'{json.dumps(self.spec[key].get('example', ''))}\'"
            else:
                value = f"{self.spec[key].get('example', '')}"
            print(f"export {self.env_prefix}_{key.upper()}={value}")

    def generate_command(self):
        """ Generate a sample command
        """
        example = []
        example.append(f"{sys.argv[0]}")
        for key in sorted(list(self.spec.keys())):
            if self.spec[key]['type'] == list:
                value = " ".join(self.spec[key].get('example', ''))
            elif self.spec[key]['type'] == dict:
                value = f"\'{json.dumps(self.spec[key].get('example', ''))}\'"
            else:
                value = self.spec[key].get('example', '')
            string = f"     --{key.lower()} {value}"
            example.append(string)
        print(" \\\n".join(example))

    def generate_docker_run(self):
        """ Generate a sample docker run
        """
        example = []
        example.append("docker run -it")
        for key in sorted(list(self.spec.keys())):
            if self.spec[key]['type'] in (dict, list):
                value = f"\'{json.dumps(self.spec[key].get('example', ''))}\'"
            else:
                value = f"{self.spec[key].get('example', '')}"
            string = f"     -e {self.env_prefix}_{key.upper()}={value}"
            example.append(string)
        example.append("     <container-name>")
        print(" \\\n".join(example))

    def generate_docker_compose(self):
        """ Generate a sample docker compose
        """
        example = {}
        example['app'] = {}
        example['app']['environment'] = []
        for key in sorted(list(self.spec.keys())):
            if self.spec[key]['type'] in (dict, list):
                value = f"\'{json.dumps(self.spec[key].get('example', ''))}\'"
            else:
                value = f"{self.spec[key].get('example', '')}"
            example['app']['environment'].append(f"{self.env_prefix}_{key.upper()}={value}")
        print(yaml.dump(example, default_flow_style=False))

    def generate_ini(self):
        """ Generate a sample ini
        """
        example = []
        example.append("[settings]")
        for key in sorted(list(self.spec.keys())):
            if self.spec[key]['type'] in [list, dict]:
                value = json.dumps(self.spec[key].get('example', ''))
            else:
                value = self.spec[key].get('example', '')
            string = f"{key.lower()}={value}"
            example.append(string)
        print("\n".join(example))

    def generate_kubernetes(self):
        """ Generate a sample kubernetes
        """
        example = {}
        example['spec'] = {}
        example['spec']['containers'] = []
        example['spec']['containers'].append({"name": '', "image": '', "env": []})
        for key, value in self.spec.items():
            if value['type'] in (dict, list):
                kvalue = f"\'{json.dumps(value.get('example', ''))}\'"
            else:
                kvalue = f"{value.get('example', '')}"
            entry = {"name": f"{self.env_prefix}_{key.upper()}", "value": kvalue}
            example['spec']['containers'][0]['env'].append(entry)
        print(yaml.dump(example, default_flow_style=False))

    def generate_drone_plugin(self):
        """ Generate a sample drone plugin configuration
        """
        example = {}
        example['pipeline'] = {}
        example['pipeline']['appname'] = {}
        example['pipeline']['appname']['image'] = ""
        example['pipeline']['appname']['secrets'] = ""
        for key, value in self.spec.items():
            if value['type'] in (dict, list):
                kvalue = f"\'{json.dumps(value.get('example', ''))}\'"
            else:
                kvalue = f"{value.get('example', '')}"
            example['pipeline']['appname'][key.lower()] = kvalue
        print(yaml.dump(example, default_flow_style=False))

    def generate_readme(self):
        """ Generate a readme with all the generators
        """
        print("## Examples of settings runtime params")
        print("### Command-line parameters")
        print("```")
        self.generate_command()
        print("```")
        print("###  Environment variables")
        print("```")
        self.generate_env()
        print("```")
        print("###  ini file")
        print("```")
        self.generate_ini()
        print("```")
        print("###  docker run")
        print("```")
        self.generate_docker_run()
        print("```")
        print("###  docker compose")
        print("```")
        self.generate_docker_compose()
        print("```")
        print("###  kubernetes")
        print("```")
        self.generate_kubernetes()
        print("```")
        print("###  drone plugin")
        print("```")
        self.generate_drone_plugin()
        print("```")




settings = ModelSettings()
