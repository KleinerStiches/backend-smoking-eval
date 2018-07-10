import json

from poc_storage.handling_json import load_dictionary, dump_dictionary, load_form_contents


def find_question_type(question_form_info):
    key_map = {
        "next_yes": "question-binary",
        "placeholder": "question-input",
        "options": "question-options"
    }

    for key in question_form_info:
        if key in key_map:
            return key_map.get(key)

    return None


def build_questions_tree():
    all_questions = load_form_contents()
    starting_question = None
    for content in all_questions["codes"]:
        if content.get('code') == "3":
            starting_question = content

    current_type = find_question_type(starting_question)

    question_tree = rec_question_tree(starting_question, current_type)

    print(json.dumps(question_tree, indent=4))


def rec_question_tree(question, question_type):
    all_questions = [content for content in load_form_contents().get('codes')]

    if not question_type:
        return question
    elif question_type == "question-binary":

        try:
            code_yes = str.split(question.get("next_yes"), '=')[1]
        except IndexError:
            return question

        question_yes = [match for match in all_questions if match.get('code') == code_yes][0]
        question_yes_type = find_question_type(question_yes)

        rec_question_tree(question_yes, question_yes_type)
        question['next_yes'] = question_yes

        try:
            code_no = str.split(question.get("next_no"), '=')[1]
        except IndexError:
            return question

        question_no = [match for match in all_questions if match.get('code') == code_no][0]
        question_no_type = find_question_type(question_no)

        rec_question_tree(question_no, question_no_type)
        question['next_no'] = question_no

    elif question_type == "question-options" or question_type == "question-input":
        try:
            next_code = str.split(question.get("next"), '=')[1]
        except IndexError:
            return question

        next_question = [match for match in all_questions if match.get('code') == next_code][0]
        next_question_type = find_question_type(next_question)

        rec_question_tree(next_question, next_question_type)
        question['next'] = next_question

    else:

        print('type not found')

    return question


build_questions_tree()


# def get_questions_until_binary(starting_question):
#
#     questions_to_next_binary = dict()
#
#     next_questions = get_next_questions(starting_question)
#
#     # None == unknown question type
#     # 1 == options or input
#     # 2 == binary
#     if not next_questions:
#         return
#     elif len(next_questions) == 2:
#         return {
#             next_questions.get("next")
#         }
#     elif len(next_questions) == 1:
#
#
# def get_next_questions(current_question):
#     current_type = find_question_type(current_question)
#     if current_type == "question-input" or current_type == "question-options":
#         next_url = current_question.get("next")
#         next_codes = str.split(next_url, '=')[1]
#     elif current_type "question-binary":
#         next_yes_url = current_question.get("next_yes")
#         next_no_url = current_question.get("next_no")
#         next_codes = [
#             str.split(next_yes_url, '=')[1],
#             str.split(next_no_url, '=')[1]
#         ]
#     else:
#         return None
#
#     all_questions = load_form_contents()
#     return [question for question in all_questions if question.get("code") == next_code]
