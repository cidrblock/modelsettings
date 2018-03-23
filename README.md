[![Build Status](https://travis-ci.org/cidrblock/modelsettings.svg?branch=master)](https://travis-ci.org/cidrblock/modelsettings)


# Model Settings

## Overview

Modelsetting is a straight-forward, easy to use python application settings manager that includes ini, environment variable, and command-line parameter support.

The necessary settings variables are declared in a yml model, which is then used to parse and .ini file, environment variables, and generate command-line arguments.

In addition to reading settings from the three sources, modelsettings also includes sample configuration generator support for:
- command-line
- environment variables (e.g., export statements)
- ini file
- docker run
- docker compose
- kubernetes
- drone plugins

## Quick start

### Build the model

Modelsettings looks for a `model_settings.yml` in the current working directory.  A simply `model_settings.yml` file might look like this:

```
env_prefix: CF
model:
  cream:
    choices:
    - True
    - False
    default: False
    example: True
    help: Would you like cream in your coffee?
    required: True
  sugar:
    choices:
    - True
    - False
    default: True
    example: True
    help: Would you like sugar in your coffee?
    required: True
  size:
    choices:
    - 10
    - 12
    - 16
    default: 12
    example: 16
    help: What size cup would you like in ounces?
    required: True
```
`env_prefix` is used as a prefix for the environment variables, this helps avoid namespace collision when running multiple python applications in the same shell.

`model` is a dictionary of required settings values.

### Import and use the module

In your application, simply import modelsettings.

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install modelsettings
```
app.py
```
from modelsettings import settings

def main():
    output = f"You ordered a {settings.SIZE} oz. cup of coffee"
    modifiers = []
    if settings.CREAM: modifiers.append("cream")
    if settings.SUGAR: modifiers.append("sugar")
    if modifiers:
        output += " with " + " and ".join(modifiers)
    output += "."
    print(output)

if __name__ == "__main__":
    main()

```
All settings are converted to uppercase and available as `settings.XXXXX`

### Command-line help

Argparse help is generated from the model:

```
$ python app.py --help
usage: app.py [-h]
              [--generate {command,docker-run,docker-compose,ini,env,kubernetes,readme,drone-plugin}]
              [--settings SETTINGS] [--cream {True,False}]
              [--sugar {True,False}] [--size {10,12,16}]

optional arguments:
  -h, --help            show this help message and exit
  --generate {command,docker-run,docker-compose,ini,env,kubernetes,readme,drone-plugin}
                        Generate a template
  --settings SETTINGS   Specify a settings file. (ie settings.dev)
  --cream {True,False}  Would you like cream in your coffee? e.g., True
  --sugar {True,False}  Would you like sugar in your coffee? e.g., True
  --size {10,12,16}     What size cup would you like in ounces? e.g., 16
```
