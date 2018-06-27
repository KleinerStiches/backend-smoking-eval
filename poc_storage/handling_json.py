import json
from pathlib import Path


base_path = Path(__file__).parents[2]


def load_form_contents():
    with open(
            '{}\\smoking_eval\\content\\form-content.json'.format(base_path),
            encoding="utf-8"
    ) as json_data:
        return json.load(json_data)


def load_dictionary():
    with open(
            '{}\\smoking_eval\\store\\questionaries.json'.format(base_path),
            encoding="utf-8"
    ) as json_data:
        return json.load(json_data)


def dump_dictionary(eval_dictionary):
    with open(
            '{}\\smoking_eval\\store\\questionaries.json'.format(base_path),
            'w',
            encoding="utf-8"
    ) as json_file:
        json.dump(eval_dictionary, json_file, indent=4, sort_keys=True)
