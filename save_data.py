from pathlib import Path
import json
from sqlite_utils import Database


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def save_data():
    json_folder = Path("json_output/")
    data = []
    for file in json_folder.iterdir():
        with open(file) as json_file:
            benchmark = flatten_json(json.load(json_file))
            del benchmark["control_data"]
            del benchmark["experiment_data"]
            data.append(benchmark)

    db = Database("django.db")
    db['bench'].insert_all(data)


if __name__ == '__main__':
    save_data()
