from poc_storage.handling_json import load_dictionary, dump_dictionary


def update_questionary(key, value):
    questionary = load_dictionary()
    question_code = key
    questionary[question_code] = value
    dump_dictionary(questionary)


def clear_questionary():
    empty_questionary = {"questionary": "questionary"}
    dump_dictionary(empty_questionary)


