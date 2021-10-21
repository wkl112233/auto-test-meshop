# _*_ coding: utf-8 _*_
import json
import logging
import os

from _pytest.config import Config


def pytest_configure(config: Config):
    default_path = os.path.join(config.rootpath, "logging.json")
    env_key = "LOG_CFG"
    default_level = logging.INFO
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            logging.config.dictConfig(json.load(f))
    else:
        logging.basicConfig(level=default_level)
