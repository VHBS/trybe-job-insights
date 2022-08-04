from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        file_csv = csv.DictReader(file, delimiter=',', quotechar='"')
        result = []
        for row in file_csv:
            result.append(row)
    return result
