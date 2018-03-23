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

## Additional command-line parameters

### `--help`

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

### `--generate`

A command-line paramter of generate is added to the application which, when used, will generate sample settings in a number of formats.

```
$ python app.py --generate env
export CF_CREAM=True
export CF_SIZE=16
export CF_SUGAR=True
```

### `--generate readme`

Markdown can be generated which includes all the available generate formats.

```
$ python app.py --generate readme >> README.md
```
## Order of operations

The .ini file is read first, then the environment variables, then the command-line parameters.

### .ini file support

The application will now support loading settings from a `settings.ini` file.

```
$ cat settings.ini
[settings]
cream=True
size=16
sugar=True
$ python app.py
You ordered a 16 oz. cup of coffee with cream and sugar.
```
An alternate settings file can be specified with the command line, this is useful during development of the application.

```
$ cat settings.dev
[settings]
cream=True
size=10
sugar=False
$ python app.py --settings settings.dev
You ordered a 10 oz. cup of coffee with cream.
$ python app.py --settings settings.dev --size 16
You ordered a 16 oz. cup of coffee with cream.
```

### Environment variable support

All settings can be stored as environment variables.  The environment variables should be prefaced with the `env_prefix` from the `model_settings.yml` file and capitalized.

```
$ export CF_CREAM=False
$ export CF_SIZE=12
$ export CF_SUGAR=True
$ python app.py
You ordered a 12 oz. cup of coffee with sugar.
$ export CF_CREAM=True
$ python app.py
You ordered a 12 oz. cup of coffee with cream and sugar.
```

### Command-line parameter support

Command line parameters take precedence over `.ini` files and environment variables.

```
$ python app.py --size 10 --sugar False --cream False
You ordered a 10 oz. cup of coffee.
$ python app.py --size 12 --sugar True --cream False
You ordered a 12 oz. cup of coffee with sugar.
$ python app.py --size 16 --sugar True --cream True
You ordered a 16 oz. cup of coffee with cream and sugar.
```

## model_settings.yml

1) The model support 5 basic python types:
  - `bool`
  - `int`
  - `float`
  - `string`
  - `list`
  - `dict`

The type is derived from the example given, and the settings variable is cast to that type.

In the example below, each supported type is shown with a corresponding yaml native example.

`example` is therefore a required property for every entry in the model.

```
bool:
  choices:
  - True
  - False
  default: False
  help: This is an integer setting
  required: False
  example: True
integer:
  default: 60
  help: This is an integer setting
  required: False
  example: 30
float:
  default: 60.5
  help: This is an integer setting
  required: False
  example: 30.5
string:
  default: string
  help: This is a string setting
  required: False
  example: string
dictionary:
  default:
    key: value
  help: This is a dict setting
  required: False
  example:
    key: value
list:
  default:
  - item1
  - item2
  help: This is a list setting
  required: False
  example:
  - item1
  - item2
```
