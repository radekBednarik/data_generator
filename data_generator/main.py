# DEBUG
from pprint import PrettyPrinter
from typing import Any, Dict, Generator

from cli_parser import parse_inputs, verify, convert_args, c_args
from generator import generate_column_data, pool_generate_columns

printer: Any = PrettyPrinter(indent=2, sort_dicts=False)

if __name__ == "__main__":
    args: Any = parse_inputs()

    if verify(args) is None:
        converted_args: c_args = convert_args(args)
        # DEBUG
        printer.pprint(converted_args)

        inputs = [(data, converted_args["rows"]) for data in converted_args["specify"]]

        result = pool_generate_columns(generate_column_data, inputs)

        print(result)
