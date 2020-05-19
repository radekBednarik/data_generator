from .cli_parser import convert_args, parse_inputs, verify
from .generator import generate_data
from .output import to_csv


def main():
    args = parse_inputs()

    print("--> CLI input parsed\r\n")

    if verify(args) is None:
        converted_args = convert_args(args)

        print("--> Parsed CLI inputs converted to dictionary.\r\n")

        result = generate_data(converted_args)

        print("--> Data generators created.\r\n")
        print("--> Data generation and saving to .csv starting... \n")

        to_csv(result, converted_args["rows"], converted_args["folder"])

        print("\n--> FINISHED.")


if __name__ == "__main__":
    main()
