import argparse
from typing import Union

# pyre-ignore
from data_generator.cli_parser import convert_args, parse_inputs, verify
from data_generator.generator import assemble_data_generators
from data_generator.output import to_csv, to_excel, to_json
from data_generator.toml import get_input


def run_cli_inputs(args: argparse.Namespace) -> Union[tuple, int]:
    if verify(args) is None:
        converted_args = convert_args(args)

        print("--> Parsed CLI inputs converted to dictionary.\r\n")

        result = assemble_data_generators(converted_args)

        print("--> Data generators created.\r\n")
        print("--> Data generation and saving starting... \n")

        return (result, converted_args)
    return 1


def run_toml_inputs(args: argparse.Namespace) -> Union[tuple, int]:
    converted_args = convert_args(args)

    print("--> Parsed CLI inputs converted to dictionary.\r\n")

    if len(converted_args["toml"]) > 0:
        for filepath in converted_args["toml"]:
            conf_dict = get_input(filepath)
            print(conf_dict)
            # hack
            converted_args["rows"] = conf_dict["rows"]

            result = assemble_data_generators(conf_dict)

            return (result, converted_args)
    return 1


def run_outputs(args: argparse.Namespace, inputs: tuple) -> None:
    if args.save_as == "json":
        to_json(inputs[0], inputs[1]["rows"], inputs[1]["folder"])
    elif args.save_as == "xlsx":
        to_excel(inputs[0], inputs[1]["rows"], inputs[1]["folder"])
    else:
        to_csv(inputs[0], inputs[1]["rows"], inputs[1]["folder"])

    print(f"""\n--> FINISHED. Find your data at '{inputs[1]["folder"]}' folder.""")


def main() -> None:
    args = parse_inputs()

    print("--> CLI input parsed\r\n")

    if hasattr(args, "specify"):
        output = run_cli_inputs(args)
        run_outputs(args, output)

    if hasattr(args, "toml"):
        output = run_toml_inputs(args)
        print(output)
        run_outputs(args, output)


if __name__ == "__main__":
    main()
