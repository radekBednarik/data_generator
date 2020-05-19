# DEBUG
from pprint import PrettyPrinter

from .cli_parser import convert_args, parse_inputs, verify
from .generator import generate_data
from .output import to_csv

printer = PrettyPrinter(indent=2, sort_dicts=False)


def main():
    args = parse_inputs()

    if verify(args) is None:
        converted_args = convert_args(args)
        # DEBUG
        printer.pprint(converted_args)

        result = generate_data(converted_args)

        print(result)

        to_csv(result, converted_args["rows"], converted_args["folder"])


if __name__ == "__main__":
    main()
