# MotherNature

MotherNature takes care of the environment and so does this library.
MotherNature is designed to make environment management easy using a single .yaml file.

Ever have this condition when you want to run a python script?

``` 
$ ENV=PRODUCTION ACCESS_TOKEN=SOMETOKEN ISPRODUCTION=FALSE SERVING_HOST=127.0.0.1 python app.py 
```

Sometimes it can even go longer. MotherNature aims at simplifying this into

```
$ python app.py PRODUCTION
```

Other variables are moved into the config file that you specify yourself.

## Dependency

* PyYaml

## Usage

Install using:

``` easy_install mothernature ```

or

``` pip install mothernature ```

To use simply do the following

```
from mothernature import Environment

env = Environment("someyml.yaml")

# This will provide the config based on the environment you set when starting the application
# and then you can do

test_env.get("DB_CONNECTION")

```

if you wish to force a default environment you can simply set it in the optional value for the constructor:

```
env = Environment("someyml.yaml", environment='DEV')

```
This will default the environment setting to the `DEV` environment when you run it.
By the way you can name your environment whatever way you please.

to you run it, all you need is

```
$ python yourscript.py YOUR_DESIRED_ENV
```

If you don't specify any default environment, it will default to COMMON environment. If you specify the default environment then it will go to the default environment that you set. Still, the environment from the CLI argument always wins.

Simple, right? You're welcome.


### Environments

At the minimum, you need to have at least 1 environments in the config

COMMON

This is where you specify the common environment variables that you can use and override in other environments.

An example config file of environments that I use is:

```
COMMON:
    DEBUG: false
    TESTING: false
    IS_PRODUCTION: False
TEST:
    TESTING: true
    API_KEY: 'test_api_key'
DEV:
    DEBUG: true
    TESTING: true
    API_KEY: 'development_api_key'
STAGE:
    DEBUG: true
    TESTING: false
    API_KEY: 'staging_api_key'
PROD:
    IS_PRODUCTION: true
    API_KEY: 'production_api_key'
```

COMMON is for common configs
TEST is for automated testing
DEV is for development both on local and dev server
STAGE is for staging server
PROD is for production server

Sample env.yml file is also available in the tests/ folder
