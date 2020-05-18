from string import ascii_letters, digits
from typing import Union
from random import randrange, choice


def _check_bounds(lower_bound: int, upper_bound: int) -> None:
    if lower_bound > upper_bound:
        raise ValueError(
            f"Lower bound'{str(lower_bound)}' cannot be bigger then the upper bound '{str(upper_bound)}'."
        )


def generate_string(lower_bound: int, upper_bound: int) -> Union[str, int]:
    """Generates random string from [A-Za-z0-9]. Lenght of the string
    is defined by CLI arguments provided by user. Basic check against lower bound being bigger 
    then upper bound is done.

    Arguments:
        lower_bound {int} -- minimum lenght of generated string
        upper_bound {int} -- maximum lenght of generated string

    Raises:
        ValueError: if lower bound is bigger than upper bound

    Returns:
        Union[str, int] -- generated str;  1: if ValueError
    
    See:
        https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    """
    base: str = "".join([ascii_letters, digits])

    try:
        _check_bounds(lower_bound, upper_bound)
        str_lenght: int = randrange(lower_bound, upper_bound + 1)
        return "".join(choice(base) for _ in range(str_lenght))

    except ValueError as e:
        print(str(e))
        return 1


def generate_int(lower_bound: int, upper_bound: int) -> int:
    """Generates random integer from inclusive interval <lower_bound, upper_bound>.

    Arguments:
        lower_bound {int} -- lowest possible value of the generated integer
        upper_bound {int} -- highest possible value of the generated integer

    Raises:
        ValueError: if lower_bound > upper_bound

    Returns:
        int -- generated integer, 1: if Value Error raised
    """
    try:
        _check_bounds(lower_bound, upper_bound)
        return randrange(lower_bound, upper_bound + 1)

    except ValueError as e:
        print(str(e))
        return 1
