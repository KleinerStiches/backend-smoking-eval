from poc_storage.handling_json import load_dictionary, dump_dictionary


def update_questionary(key, value):
    questionary = load_dictionary()
    question_code = key
    questionary[question_code] = value
    dump_dictionary(questionary)


def questionary_contains_answer(question_code):
    questionary = load_dictionary()
    if question_code in questionary.keys():
        return questionary[question_code]
    else:
        return None


def remove_answers_until(question_code):
    questionary = load_dictionary()

    for answer_code in reversed(list(questionary.keys())):
        if answer_code.isnumeric():
            if int(answer_code) > int(question_code):
                questionary.pop(answer_code)

    dump_dictionary(questionary)


def clear_questionary():
    empty_questionary = {"questionary": "questionary"}
    dump_dictionary(empty_questionary)
