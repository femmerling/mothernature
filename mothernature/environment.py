import os
import yaml


class Environment():

    def __init__(self, config_file):
        with open(config_file, "r") as config:
            self.config = yaml.load(config)

    def get_config(self):
        os_env = os.environ.get("ENV")

        environment = os_env if os_env else "DEVELOPMENT"
        if not environment:
            raise Exception(
                "You have not specify this environment in your config file")

        env_data = self.config.get(environment)
        return self._combine_env_data(env_data)

    def _combine_env_data(self, env_data):
        config = self.config.get("COMMON")
        if not config:
            return env_data

        for key, value in env_data.iteritems():
            config[key] = value
        return config

    def set_config(self, environment, key, value):
        self.config.get(environment)[key] = value
        return self.get_config(environment)
