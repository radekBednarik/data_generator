# pyre-ignore
from tomlkit import parse


def get_input(filepath: str) -> dict:
    with open(filepath, mode="r", encoding="utf-8") as f:
        return parse(f.read())
