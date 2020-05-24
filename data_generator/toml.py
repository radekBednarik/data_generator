# pyre-ignore
import sys
from os import getcwd
from os.path import join

from tomlkit import parse


def get_input(filepath: str) -> dict:
    """Returns TOML file content as dict.

    Arguments:
        filepath {str} -- filepath to TOML file

    Returns:
        dict -- TOML content as dict
    """
    filepath = join(getcwd(), filepath)

    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            return parse(f.read())
    except FileNotFoundError as e:
        print(f"Exception in func 'get_input': {str(e)}")
        sys.exit(1)
