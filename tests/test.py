import unittest

from mothernature import Environment


class EnvironmentTest(unittest.TestCase):

    def setUp(self):
        self.config = Environment("env.yml")

    def test_environment_test(self):
        config = self.config.get_config("TEST")
        self.assertTrue(
            config.get("TESTING"),
            "TESTING should be True")

    def test_environment_dev(self):
        config = self.config.get_config("DEVELOPMENT")
        self.assertTrue(
            config.get("DEBUG"),
            "DEBUG should be True")

    def test_environment_stage(self):
        config = self.config.get_config("STAGING")
        self.assertTrue(
            config.get("DEBUG"),
            "DEBUG should be True")

    def test_environment_prod(self):
        config = self.config.get_config("PRODUCTION")
        self.assertTrue(
            config.get("IS_PRODUCTION"),
            "IS_PRODUCTION should be True")


class EnvironmentDefaultTest(unittest.TestCase):

    def setUp(self):
        self.config = Environment("env.yml", environment="TEST")

    def test_default_environment(self):
        self.assertTrue(self.config.get("TESTING"),
            "TESTING should be true if TEST environment is true")
