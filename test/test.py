# coding: utf-8
""" hardware TestCases
"""
import unittest
import os
import sys
import importlib
from unittest import mock
import modelsettings
import io
import yaml



class TestHardwareController(unittest.TestCase):
    """ HardwareController integration test stubs """

#pylint: disable=E1101
    # default tests
    def test_bool_default(self):
        """
        Test BOOL_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.BOOL_DEFAULT, False, settings.BOOL_DEFAULT)
    def test_integer_default(self):
        """
        Test INTEGER_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.INTEGER_DEFAULT, 60, settings.INTEGER_DEFAULT)
    def test_float_default(self):
        """
        Test FLOAT_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.FLOAT_DEFAULT, 60.5, settings.FLOAT_DEFAULT)
    def test_string_default(self):
        """
        Test STRING_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_DEFAULT, "string", settings.STRING_DEFAULT)
    def test_dict_default(self):
        """
        Test DICTIONARY_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertDictEqual(settings.DICTIONARY_DEFAULT, {"key": "value"}, settings.DICTIONARY_DEFAULT)
    def test_list_default(self):
        """
        Test LIST_DEFAULT
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.LIST_DEFAULT, ["item1", "item2"], settings.LIST_DEFAULT)

    # ini file tests
    def test_bool_ini(self):
        """
        Test BOOL_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.BOOL_INI, True, settings.BOOL_INI)
    def test_integer_ini(self):
        """
        Test INTEGER_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.INTEGER_INI, 10, settings.INTEGER_INI)
    def test_float_ini(self):
        """
        Test FLOAT_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.FLOAT_INI, 10.10, settings.FLOAT_INI)
    def test_string_ini(self):
        """
        Test STRING_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_INI, "list_string", settings.STRING_INI)
    def test_dict_ini(self):
        """
        Test DICTIONARY_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertDictEqual(settings.DICTIONARY_INI, {"key": "ini_value"}, settings.DICTIONARY_INI)
    def test_list_ini(self):
        """
        Test LIST_INI
        """
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.LIST_INI, ["list_item1", "list_item2"], settings.LIST_INI)
    # env var tests (set in tox.ini)
    def test_bool_envar(self):
        """
        Test BOOL_ENVAR
        """
        os.environ["UT_BOOL_ENVAR"] = "True"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.BOOL_ENVAR, True, settings.BOOL_ENVAR)
        del os.environ["UT_BOOL_ENVAR"]

    def test_integer_envar(self):
        """
        Test INTEGER_ENVAR
        """
        os.environ["UT_INTEGER_ENVAR"] = "20"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.INTEGER_ENVAR, 20, settings.INTEGER_ENVAR)
        del os.environ["UT_INTEGER_ENVAR"]

    def test_float_envar(self):
        """
        Test FLOAT_ENVAR
        """
        os.environ["UT_FLOAT_ENVAR"] = "20.20"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.FLOAT_ENVAR, 20.20, settings.FLOAT_ENVAR)
        del os.environ["UT_FLOAT_ENVAR"]

    def test_string_envar(self):
        """
        Test STRING_ENVAR
        """
        os.environ["UT_STRING_ENVAR"] = "envar_string"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_ENVAR, "envar_string", settings.STRING_ENVAR)
        del os.environ["UT_STRING_ENVAR"]

    def test_dict_envar(self):
        """
        Test DICTIONARY_ENVAR
        """
        os.environ["UT_DICTIONARY_ENVAR"] = '{"key": "envar_value"}'
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertDictEqual(settings.DICTIONARY_ENVAR,
                             {"key": "envar_value"},
                             settings.DICTIONARY_ENVAR)
        del os.environ["UT_DICTIONARY_ENVAR"]

    def test_list_envar(self):
        """
        Test LIST_ENVAR
        """
        os.environ["UT_LIST_ENVAR"] = '["envar_item1", "envar_item2"]'
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.LIST_ENVAR, ["envar_item1", "envar_item2"], settings.LIST_ENVAR)
        del os.environ["UT_LIST_ENVAR"]

    def test_bool_command(self):
        """
        Test BOOL_COMMAND
        """
        testargs = ["--bool_command", "True"]
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.BOOL_COMMAND, True, settings.BOOL_COMMAND)

    def test_integer_command(self):
        """
        Test INTEGER_COMMAND
        """
        testargs = ["--integer_command", "30"]
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.INTEGER_COMMAND, 30, settings.INTEGER_COMMAND)

    def test_float_command(self):
        """
        Test FLOAT_COMMAND
        """
        testargs = ["--float_command", "30.5"]
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.FLOAT_COMMAND, 30.5, settings.FLOAT_COMMAND)

    def test_string_command(self):
        """
        Test STRING_COMMAND
        """
        testargs = ["--string_command", "command_string"]
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_COMMAND, "command_string", settings.STRING_COMMAND)

    def test_list_command(self):
        """
        Test LIST_COMMAND
        """
        testargs = ["--list_command", "command_item1", "command_item2"]
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.LIST_COMMAND,
                         ['command_item1', 'command_item2'],
                         settings.LIST_COMMAND)

    def test_dictionary_command(self):
        """
        Test DICTIONARY_COMMAND
        """
        testargs = ["--dictionary_command", '{"key": "command_value"}']
        sys.argv[1:] = testargs
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertDictEqual(settings.DICTIONARY_COMMAND,
                             {"key": "command_value"},
                             settings.DICTIONARY_COMMAND)

    # test the generators
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_env(self, output):
        """
        Test GENERATE_ENV
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'env']
            sys.argv[1:] = testargs
            for entry in output.getvalue().splitlines():
                os.system(entry)
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 24, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_ini(self, output):
        """
        Test GENERATE_INI
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'ini']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 25, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_command(self, output):
        """
        Test GENERATE_COMMAND
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'command']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 25, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_docker_run(self, output):
        """
        Test GENERATE_DOCKER_RUN
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'docker-run']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 26, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_docker_compose(self, output):
        """
        Test GENERATE_DOCKER_COMPOSE
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'docker-compose']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
            dikt = yaml.load(output.getvalue())
            for entry in dikt['app']['environment']:
                os.system(f"export {entry}")
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 27, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_kubernetes(self, output):
        """
        Test GENERATE_KUBERNETES
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'kubernetes']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
            dikt = yaml.load(output.getvalue())
            for value in dikt['spec']['containers'][0]['env']:
                os.system(f"export {value['name']}={value['value']}")
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 54, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_readme(self, output):
        """
        Test GENERATE_README
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'readme']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
            dikt = yaml.load(output.getvalue())
            for value in dikt['spec']['containers'][0]['env']:
                os.system(f"export {value['name']}={value['value']}")
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 232, output.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_drone_plugin(self, output):
        """
        Test GENERATE_DRONE_PLUGIN
        """
        with self.assertRaises(SystemExit):
            testargs = ["--generate", 'drone-plugin']
            sys.argv[1:] = testargs
            importlib.reload(modelsettings)
            dikt = yaml.load(output.getvalue())
            for value in dikt['spec']['containers'][0]['env']:
                os.system(f"export {value['name']}={value['value']}")
            importlib.reload(modelsettings)
        self.assertEqual(len(output.getvalue().splitlines()), 29, output.getvalue())

    # test a required setting
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_bool_required(self, output):
        """
        Test BOOL_REQUIRED
        """
        os.environ["MODEL_SETTINGS"] = "model_settings_br.yml"
        with self.assertRaises(SystemExit):
            importlib.reload(modelsettings)
        self.assertIn("is a required setting", output.getvalue())
        del os.environ["MODEL_SETTINGS"]

    # test the hierarchy
    def test_env_overrides_ini(self):
        """
        Test ENV_OVERRIDES_INI
        """
        os.environ["UT_STRING_INI"] = "env_override"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_INI, "env_override", settings.STRING_INI)
        del os.environ["UT_STRING_INI"]

    def test_command_over_env_over_ini(self):
        """
        Test COMMAND_OVER_ENV_OVER_INI
        """
        testargs = ["--string_ini", "command_override"]
        sys.argv[1:] = testargs
        os.environ["UT_STRING_INI"] = "env_override"
        importlib.reload(modelsettings)
        from modelsettings import settings
        self.assertEqual(settings.STRING_INI, "command_override", settings.STRING_INI)
        del os.environ["UT_STRING_INI"]

    # using a different model file
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_missing_settings(self, output):
        """
        Test MODEL_SETTINGS
        """
        os.environ["MODEL_SETTINGS"] = "foo.yml"
        with self.assertRaises(SystemExit):
            importlib.reload(modelsettings)
            self.assertIn("Error finding", output.getvalue())
        del os.environ["MODEL_SETTINGS"]

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_missing_ini(self, output):
        """
        Test MISSING_SETTINGS
        """
        testargs = ["--settings", "foo.ini"]
        sys.argv[1:] = testargs
        with self.assertRaises(SystemExit):
            importlib.reload(modelsettings)
            self.assertIn("Error finding", output.getvalue())
        sys.argv[1:] = []

if __name__ == '__main__':
    unittest.main()
