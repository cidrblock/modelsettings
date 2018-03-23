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
