# DEBUG
from pprint import PrettyPrinter
from typing import Any, Optional, Dict, Generator

from cli_parser import parse_inputs, verify, convert_args, c_args
from generator import generate_string, generate_int, generate_float, generate_column_data

printer: Any = PrettyPrinter(indent=2, sort_dicts=False)

if __name__ == "__main__":
    args: Any = parse_inputs()

    if verify(args) is None:
        converted_args: c_args = convert_args(args)
        # DEBUG
        printer.pprint(converted_args)
