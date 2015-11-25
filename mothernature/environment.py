import os
import yaml


class Environment():
    environments = ["TEST", "DEVELOPMENT", "STAGING", "PRODUCTION"]
    config = None
    common = None
    test = None
    dev = None
    stage = None
    prod = None

    def __init__(self, config_file):
        with open(config_file, "r") as config:
            self.config = yaml.load(config)
        self.initialize_value()

    def get_config(self):
        environment = os.environ.get("HOME")
        if not environment:
            environment = "DEVELOPMENT"
        if environment not in self.environments:
            raise Exception("that is not a valid environment")

        environment_methods = {
            "TEST": self._get_test_config,
            "DEVELOPMENT": self._get_development_config,
            "STAGING": self._get_staging_config,
            "PRODUCTION": self._get_production_config
        }

        config = environment_methods.get(environment)
        return config()

    def _get_test_config(self):
        return self._combine_env_data(self.test)

    def _get_development_config(self):
        return self._combine_env_data(self.dev)

    def _get_staging_config(self):
        return self._combine_env_data(self.stage)

    def _get_production_config(self):
        return self._combine_env_data(self.prod)

    def _combine_env_data(self, env_data):
        config = self.common
        for key, value in env_data.iteritems():
            config[key] = value
        return config

    def set_config(self, environment, key, value):
        self.config.get(environment)[key] = value
        self.initialize_value()
        return self.get_config(environment)

    def initialize_value(self):
        self.common = self.config.get("COMMON")
        self.test = self.config.get("TEST")
        self.dev = self.config.get("DEVELOPMENT")
        self.stage = self.config.get("STAGING")
        self.prod = self.config.get("PRODUCTION")
