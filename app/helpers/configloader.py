import json

class ConfigLoader:
    def __init__(self):
        with open('resources/config.json', 'r') as file:
            self.config = json.load(file)

    def load_default(self):
        return self.config.get('default')

    def load_override(self, override=None):
        if override in self.config.keys():
            return self.config.get(override)

    def load(self, override=None):
        ret_dict = self.load_default()
        # if override is not None:
            # ret_dict.update(self.load_override(override))
        return ret_dict


class InvalidConfigKeyError(Exception):
    def __init__(self, message, error):
        super(InvalidConfigKeyError, self).__init__(message)
        self.error = error