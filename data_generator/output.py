import csv
from datetime import datetime as dt
from os.path import join, isdir
from os import makedirs
from tqdm import tqdm


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

        for _ in tqdm(range(rows_count)):
            row = {}

            for header, data_generator in list(data.items()):
                # key will never be there, dict is empty for each cycle
                if header not in row:
                    row[header] = next(data_generator)

            writer.writerow(row)
