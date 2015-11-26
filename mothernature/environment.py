import sys
import yaml


class Environment():

    def __init__(self, config_file):
        self.environment = "COMMON"
        if len(sys.argv) > 1:
            self.environment = sys.argv[1]
        with open(config_file, "r") as config:
            self.all_config = yaml.load(config)

    def get(self, key):
        env = self.get_config()
        return env.get(key)

    def get_config(self):
        env_data = self.all_config.get(self.environment)
        if self.environment == "COMMON" and not env_data:
            raise Exception(
                "You haven't specify COMMON configuration in your config file")

        if not env_data:
            raise Exception(
                "You have not specify this environment in your config file")

        return self._combine_env_data(env_data)

    def _combine_env_data(self, env_data):
        config = self.all_config.get("COMMON")
        if not config:
            return env_data

        for key, value in env_data.iteritems():
            config[key] = value
        return config

    def set_config(self, environment, key, value):
        self.all_config.get(environment)[key] = value
        return self.get_config(environment)
