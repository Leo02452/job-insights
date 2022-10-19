import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        content_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        content_list = list(content_reader)
    return content_list
