import unittest

from app.helpers.configloader import InvalidConfigKeyError, ConfigLoader


class ConfigLoaderTests(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(InvalidConfigKeyError, ConfigLoader().load_override('invalid_key'))