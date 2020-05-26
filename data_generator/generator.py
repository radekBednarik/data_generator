from datetime import MAXYEAR, MINYEAR
from datetime import datetime as dt
from random import choice, randrange, uniform
from string import ascii_letters, digits
from typing import Callable, Generator, Union


def _check_bounds(lower_bound: float, upper_bound: float) -> None:
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


def _generator(
    rand_val_creator: Callable, upper_bound=None, lower_bound=None, date_template=None
) -> Generator:
    """Yields random value from given <rand_val_creator> Callable.

    Arguments:
        rand_val_creator {Callable} -- func returning random data
        upper_bound -- upper bound of the interval from which random data is created
        lower_bound -- lower bound of the interval from which random data is created
        date_template -- template for date

    Yields:
        random value 
    """
    if (upper_bound is not None) and (lower_bound is not None):
        while True:
            yield rand_val_creator(lower_bound, upper_bound)

    if date_template is not None:
        while True:
            yield rand_val_creator(date_template)

    if (upper_bound is None) and (lower_bound is None) and (date_template is None):
        while True:
            yield rand_val_creator()


def random_string(lower_bound: int, upper_bound: int) -> Union[int, str]:
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


def random_int(lower_bound: int, upper_bound: int) -> int:
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


def random_float(lower_bound: float, upper_bound: float) -> Union[float, int]:
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


def random_date(format_template: str) -> Union[int, str]:
    """Returns date str formatted as <format_template> specifies.

    Templating supports:
        %Y, %m, %d, %H, %M, %S, %f, _, -

    Arguments:
        format_template {str} -- format template for date object

    Returns:
        str -- date formatted as <format_template>
    """
    try:
        year = randrange(MINYEAR, MAXYEAR + 1)
        month = randrange(1, 13)
        day = randrange(1, 31) if month != 2 else randrange(1, 29)
        hour = randrange(0, 24)
        minute = randrange(0, 60)
        second = randrange(0, 60)
        microsecond = randrange(0, 1000000)

        date_ = dt(
            year,
            month,
            day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
        )

        return date_.strftime(format_template)

    except Exception as e:
        print(f"Exception raised in func 'random_date': {str(e)}")
        return 1


def random_timestamp() -> Union[float, int]:
    """Returns POSIX timestamp as float.

    Returns:
        Union[float, int] -- POSIX timestamp as float; 1: if NOK

    See:
        https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp
    """
    try:
        year = randrange(1970, MAXYEAR + 1)
        month = randrange(1, 13)
        day = randrange(1, 31) if month != 2 else randrange(1, 29)
        hour = randrange(0, 24)
        minute = randrange(0, 60)
        second = randrange(0, 60)
        microsecond = randrange(0, 1000000)

        date_ = dt(
            year,
            month,
            day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
        )
        return date_.timestamp()

    except Exception as e:
        print(f"Exception raised in func 'random_timestamp': {str(e)}")
        return 1


def create_data_generator(assigned_args: dict) -> Union[Generator, int]:
    """Returns data generator for given arguments datatype.

    Arguments:
        assigned_args -- parsed cli input for given datatype, like int, str, float, date

    Returns:
        generator object; 1: if NOK
    """
    aa = assigned_args

    if aa["data_type"] == "str":
        return _generator(
            random_string, lower_bound=aa["lower_bound"], upper_bound=aa["upper_bound"]
        )

    if aa["data_type"] == "int":
        return _generator(
            random_int, lower_bound=aa["lower_bound"], upper_bound=aa["upper_bound"]
        )

    if aa["data_type"] == "float":
        return _generator(
            random_float, lower_bound=aa["lower_bound"], upper_bound=aa["upper_bound"]
        )

    if aa["data_type"] == "date":
        return _generator(random_date, date_template=aa["format_template"])

    if aa["data_type"] == "timestamp":
        return _generator(random_timestamp)

    return 1


def assemble_data_generators(converted_args: dict) -> dict:
    """Returns dict with all columns names as keys and data generators as values.

    Arguments:
        converted_args -- converted CLI args to dict

    Returns:
        dict with data generators for all columns
    """
    output = {}

    for data in converted_args["specify"]:
        if data["column_name"] not in list(output.keys()):
            output[data["column_name"]] = None

        output[data["column_name"]] = create_data_generator(data)

    return output
