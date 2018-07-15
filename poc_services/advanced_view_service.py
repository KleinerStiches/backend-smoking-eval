import json

from poc_storage.handling_json import load_form_contents


# def flatten_tree(_tree):
#     root = _tree['root']
#     return flatten_rec(root)
#
#
# def flatten_rec(node):
#     try:
#         question_type = node['question_type']
#     except KeyError:
#         question_type = None
#
#     if not question_type:
#         return node
#     elif question_type == "question-binary":
#         return [node['code'], [flatten_rec(node['next_yes']), flatten_rec(node['next_no'])]]
#     else:
#         return [node['code'], [flatten_rec(node['next'])]]

# def flatten_tree(_tree):
#     valid_keys = ["root", "next_yes", "next_no", "next"]
#     # return [[k] + [_tree[k].get(x) for x in valid_keys if x in valid_keys] for k in _tree]
#     # return [[k, v] for k, v in _tree.items()]
#     return _tree.iteritems()


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

    #return rec_question_tree(starting_question, current_type)
    question_tree = dict()
    question_tree['code'] = "root"
    question_tree['question_type'] = "question-input"
    question_tree['next'] = rec_question_tree(starting_question, current_type)
    return question_tree


# TODO the code with the try until min question_..._type is duplicated and
# TODO can be out sourced to a separate function
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
        question['question_type'] = question_type
        question['next_yes'] = question_yes

        try:
            code_no = str.split(question.get("next_no"), '=')[1]
        except IndexError:
            return question

        question_no = [match for match in all_questions if match.get('code') == code_no][0]
        question_no_type = find_question_type(question_no)

        rec_question_tree(question_no, question_no_type)
        question['question_type'] = question_type
        question['next_no'] = question_no

    elif question_type == "question-options" or question_type == "question-input":
        try:
            next_code = str.split(question.get("next"), '=')[1]
        except IndexError:
            return question

        next_question = [match for match in all_questions if match.get('code') == next_code][0]
        next_question_type = find_question_type(next_question)

        rec_question_tree(next_question, next_question_type)
        question['question_type'] = question_type
        question['next'] = next_question

    else:

        print('type not found')

    return question

# tree = build_questions_tree()
#
# print(json.dumps(tree, indent=4))
#
# print(flatten_tree(tree))
