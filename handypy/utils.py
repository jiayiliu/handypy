import logging
import os
from argparse import Namespace

import yaml

logger = logging.getLogger(__name__)


def validate_folder(folder:str) -> None:
    if os.path.isfile(folder):
        raise FileExistsError("Target folder path exists by file")
    os.makedirs(os.path.abspath(folder), exist_ok=True)


def set_log(level: str='info') -> None:
    try:
        level = getattr(logging, level.upper())
    except AttributeError:
        level = logging.INFO
        print("Logging level (%s) not match, use default level (info)" % level)

    logging.basicConfig(level=level,
                        format='%(name)-25s:%(funcName)20s: %(levelname)-8s: %(message)s')


def load_yaml_namespace(filename: str) -> Namespace:
    config = yaml.safe_load(open(filename))
    return Namespace(**config)
