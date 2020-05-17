from string import ascii_letters, digits
from typing import Union
from random import randrange, choice


def generate_string(lower_bound: int, upper_bound: int) -> Union[str, int]:
    """Generates random string from [A-Za-z0-9]. Lenght of the string
    is defined by CLI arguments provided by user. Basic check against lower bound being bigger 
    then upper bound is done.

    Arguments:
        specs {Dict[str, Union[Type[str], str, int]]} -- specifications for string generation provided by func
        cli_parser.convert_args()

    Raises:
        ValueError: if lower bound is bigger than upper bound

    Returns:
        Union[str, int] -- generated str, 1, if error
    
    See:
        https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    """
    base: str = "".join([ascii_letters, digits])

    try:
        if lower_bound > upper_bound:
            raise ValueError(
                f"Lower bound of string '{str(lower_bound)}' cannot be bigger then upper bound '{str(upper_bound)}'."
            )
        str_lenght: int = randrange(lower_bound, upper_bound + 1)

        return "".join(choice(base) for _ in range(str_lenght))

    except ValueError as e:
        print(str(e))
        return 1
