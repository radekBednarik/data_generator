# DEBUG
from pprint import PrettyPrinter

from cli_parser import convert_args, parse_inputs, verify
from generator import generate_data

printer = PrettyPrinter(indent=2, sort_dicts=False)

if __name__ == "__main__":
    args = parse_inputs()

    if verify(args) is None:
        converted_args = convert_args(args)
        # DEBUG
        printer.pprint(converted_args)

        inputs = [(data, converted_args["rows"]) for data in converted_args["specify"]]

        result = generate_data(converted_args)

        print(result)

        for a in result["column3"]:
            print(a)
