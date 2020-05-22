import csv
from datetime import datetime as dt
from os import makedirs
from os.path import isdir, join

# pyre-ignore
from jsonstreams import Stream, Type

# pyre-ignore
from tqdm import tqdm


def _check_dir(dirpath: str) -> None:
    """Checks for <dirpath> existence and creates it recursively, if not found.

    Arguments:
        dirpath -- path to directory
    """
    if not isdir(dirpath):
        makedirs(dirpath, exist_ok=True)


def to_csv(data: dict, rows_count: int, output_folder: str) -> None:
    """Saves generated data into .csv file.

    Arguments:
        data -- converted CLI args as dict
        rows_count -- number of rows generated excluding header
        output_folder -- folder to save generated .csv file into
    """
    headers = list(data.keys())
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.csv"
    filepath = join(output_folder, filename)

    _check_dir(output_folder)

    with open(filepath, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for _ in tqdm(range(rows_count)):
            row = {}

            for header, data_generator in list(data.items()):
                # key will never be there, dict is empty for each cycle
                if header not in row:
                    row[header] = next(data_generator)

            writer.writerow(row)


def to_json(data: dict, rows_count: int, output_folder: str) -> None:
    """Saves generated data into .json file.

    Arguments:
        data {dict} -- converted CLI args as dict
        rows_count {int} -- number of ros generated excluding "header"
        output_folder {str} -- folder to save generated .json file into
    """
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.json"
    filepath = join(output_folder, filename)

    with Stream(Type.object, filename=filepath) as s:
        dict_ = {}
        for _ in tqdm(range(rows_count)):
            for header, data_generator in list(data.items()):
                if header not in dict_:
                    dict_[header] = []
                dict_[header].append(next(data_generator))
            s.write("data", dict_)
