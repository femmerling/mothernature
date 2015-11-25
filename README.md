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

### Environments

At the minimum, you need to have at least 1 environments in the config

```COMMON```

This is where you specify the common environment variables that you can use and override in other environments 

Sample env.yml file is available in the tests/ folder