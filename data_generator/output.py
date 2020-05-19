import csv
from datetime import datetime as dt
from os.path import join, isdir
from os import makedirs


def _check_dir(dirpath):
    if not isdir(dirpath):
        makedirs(dirpath, exist_ok=True)


def to_csv(data, rows_count, output_folder):
    headers = list(data.keys())
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data_{timestamp}.csv"

    _check_dir(output_folder)

    with open(
        join(output_folder, filename), mode="w", encoding="utf-8", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for _ in range(rows_count):
            print(next(list(data.values())[0]))
