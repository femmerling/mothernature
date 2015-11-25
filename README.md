# MotherNature

MotherNature takes care of the environment and so does this library.
MotherNature is designed to make environment management easy using a single .yaml file.

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

## Supported Environments

Currently Mothernature supports 4 main environments:

* TEST
* DEVELOPMENT
* STAGING
* PRODUCTION

Sample env.yml file is available in the tests/ folder