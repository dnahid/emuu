""" Configuration file helper module.
"""

__version__ = "0.1"
__author__ = "Nahidul Islam"

import yaml
from pathlib import Path

DEFAULT_RELATIVE_PATH = Path.cwd().joinpath("emuu")
DEFAULT_FILE_NAME = "config.yml"


class ConfigHelper:
    def __init__(self, file_path=None, file_name=None):
        self.__relative_path = DEFAULT_RELATIVE_PATH if file_path is None else file_path
        self.__file_name = DEFAULT_FILE_NAME if file_name is None else file_name
        self.__config = {}
        self.__parse()

    def get_base_url(self):
        return self.__config.get("source")

    def get_destination_path(self):
        return Path(DEFAULT_RELATIVE_PATH) / self.__config.get("destination")

    def get_file_names(self):
        return self.__config.get("files")

    def __parse(self):
        try:
            with open(Path(self.__relative_path) / self.__file_name, "r") as config_file:
                self.__config = yaml.load(config_file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print("Configuration file doesn't exist!")

    def __str__(self):
        return "Configurations are loaded from {}".format(self.__file_name)


if __name__ == "__main__":
    ch = ConfigHelper()
    print(ch.get_base_url())
    print(ch.get_destination_path())
    print(ch.get_file_names())
