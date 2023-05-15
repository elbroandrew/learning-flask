import os.path

import yaml

"""
from https://www.youtube.com/watch?v=bA8RBBboApI tutorial
"""


class Config:

    __slots__ = [
        "_path",
        "DEBUG",
        "SECRET_KEY",
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    ]

    def __init__(self, yaml_file_path: str) -> None:
        self._path = yaml_file_path
        self._read()

    def _read(self) -> None:
        if not os.path.exists(self._path):
            raise AttributeError(f"yaml config doesn't exist: {self._path}")

        with open(self._path) as config_file:
            config_content = config_file.read()
            config_yaml = yaml.safe_load(config_content)

        for k, v in config_yaml.items():
            k = k.upper()
            if k in self.__slots__:
                setattr(self, k, v)
