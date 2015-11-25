# MotherNature

MotherNature takes care of the environment and so does this library.
MotherNature is designed to make environment management easy using a single .yaml file.

Ever have this condition when you want to run a python script?

``` 
$ ENV=PRODUCTION ACCESS_TOKEN=SOMETOKEN ISPRODUCTION=FALSE SERVING_HOST=127.0.0.1 python app.py 
```

Sometimes it can even go longer. MotherNature aims at simplifying this into

```
$ ENV=YOUR_ENV python app.py
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
test_env = env.get_config()

# and then you can do

test_env.get("DB_CONNECTION")

```

when you run it, all you need is

```
$ ENV=YOUR_DESIRED_ENV
```

If you don't specify it, it will default to COMMON environment.

Simple, right? You're welcome.


### Environments

At the minimum, you need to have at least 1 environments in the config

```COMMON```

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