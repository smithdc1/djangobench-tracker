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


json_folder = Path("json_output/")
data = []
for file in json_folder.iterdir():
    with open(file) as json_file:
        data.append(flatten_json(json.load(json_file)))

db = Database("django.db")
db['bench'].insert_all(data)
