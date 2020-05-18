from multiprocessing import get_context
from random import choice, randrange, uniform
from string import ascii_letters, digits


def _check_bounds(lower_bound, upper_bound):
    """Checks, whether lower bound of the interval has not bigger value than upper bound.
    Raises ValueError, if it is so.

    Arguments:
        lower_bound -- provided value of lower bound
        upper_bound -- provided value of upper bound

    Raises:
        ValueError: -- prints f"Lower bound'{str(lower_bound)}' cannot be bigger then the upper bound '{str(upper_bound)}'."
    """
    if lower_bound > upper_bound:
        raise ValueError(
            f"Lower bound'{str(lower_bound)}' cannot be bigger then the upper bound '{str(upper_bound)}'."
        )


def generate_string(lower_bound, upper_bound):
    """Generates random string from [A-Za-z0-9]. Lenght of the string
    is defined by CLI arguments provided by user. Basic check against lower bound being bigger 
    then upper bound is done.

    Arguments:
        lower_bound -- minimum lenght of generated string
        upper_bound -- maximum lenght of generated string

    Raises:
        ValueError: if lower bound is bigger than upper bound

    Returns:
        generated str;  1: if ValueError
    
    See:
        https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    """
    base = "".join([ascii_letters, digits])

    try:
        _check_bounds(lower_bound, upper_bound)
        str_lenght = randrange(lower_bound, upper_bound + 1)
        return "".join(choice(base) for _ in range(str_lenght))

    except ValueError as e:
        print(str(e))
        return 1


def generate_int(lower_bound, upper_bound):
    """Generates random integer from inclusive interval <lower_bound, upper_bound>.

    Arguments:
        lower_bound -- lowest possible value of the generated integer
        upper_bound -- highest possible value of the generated integer

    Raises:
        ValueError: if lower_bound > upper_bound

    Returns:
        generated integer, 1: if Value Error raised
    """
    try:
        _check_bounds(lower_bound, upper_bound)
        return randrange(lower_bound, upper_bound + 1)

    except ValueError as e:
        print(str(e))
        return 1


def generate_float(lower_bound, upper_bound):
    """Generates random float from given interval.

    Given the rounding, the interval is (not) right-side inclusive, i.e.
    <lower_bound, upper_bound> or <lower_bound, upper_bound). Check documentation
    in See section.

    Arguments:
        lower_bound -- lowest possible value of generated float
        upper_bound -- highest possible value of generated float, may be not included
    
    Raises:
        ValueError: if lower_bound > upper_bound

    Returns:
        generated float, 1: if ValueError raised

    See:
        https://docs.python.org/3/library/random.html#random.uniform
    """
    try:
        _check_bounds(lower_bound, upper_bound)
        return uniform(lower_bound, upper_bound)

    except ValueError as e:
        print(str(e))
        return 1


def generate_column_data(assigned_args, rows_count):
    aa = assigned_args

    if aa["data_type"] is str:
        return [
            generate_string(aa["lower_bound"], aa["upper_bound"])
            for _ in range(rows_count)
        ]

    if aa["data_type"] is int:
        return [
            generate_int(aa["lower_bound"], aa["upper_bound"])
            for _ in range(rows_count)
        ]

    if aa["data_type"] is float:
        return [
            generate_float(aa["lower_bound"], aa["upper_bound"])
            for _ in range(rows_count)
        ]

    return None


def pool_generate_columns(column_data_generator, args):
    with get_context("spawn").Pool(maxtasksperchild=1) as p:
        result = p.starmap(column_data_generator, args)

    return result
