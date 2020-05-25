import csv
import json
from datetime import datetime as dt
from os import makedirs
from os.path import isdir, join

# pyre-ignore
from tqdm import tqdm
# pyre-ignore
from xlsxwriter import Workbook


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
        rows_count {int} -- number of rows generated excluding "header"
        output_folder {str} -- folder to save generated .json file into
    """
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.json"
    filepath = join(output_folder, filename)

    _check_dir(output_folder)

    output = {}

    for _ in tqdm(range(rows_count)):
        for header, data_generator in list(data.items()):
            if header not in output:
                output[header] = []

            output[header].append(next(data_generator))

    with open(filepath, mode="w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


def to_excel(data: dict, rows_count: int, output_folder: str) -> None:
    """Saves generated data into .xlsx file.

    Arguments:
        data {dict} -- converted CLI args as dict
        rows_count {int} -- number of rows generated excluding "header"
        output_folder {str} -- folder to save generated .xlsx file into
    """
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.xlsx"
    filepath = join(output_folder, filename)

    _check_dir(output_folder)

    workbook = Workbook(filepath, {"constant_memory": True})
    sheet = workbook.add_worksheet()

    for col, header in enumerate(list(data.keys())):
        sheet.write(0, col, header)

    for row in tqdm(range(1, rows_count + 1)):
        for col, data_generator in enumerate(list(data.values())):
            sheet.write(row, col, next(data_generator))

    workbook.close()
