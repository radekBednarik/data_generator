import csv
from datetime import datetime as dt
from os import makedirs
from os.path import isdir, join

from tqdm import tqdm


def _check_dir(dirpath):
    """Checks for <dirpath> existence and creates it recursively, if not found.

    Arguments:
        dirpath -- path to directory
    """
    if not isdir(dirpath):
        makedirs(dirpath, exist_ok=True)


def to_csv(data, rows_count, output_folder):
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
