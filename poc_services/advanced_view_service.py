import json
import random
import uuid

from poc_storage.handling_json import load_form_contents


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
    collapse_question_id = 0
    question_tree = dict()
    question_tree['id'] = "root"
    question_tree['code'] = "root"
    question_tree['question_type'] = "question-input"
    question_tree['next'] = rec_question_tree(starting_question, current_type, collapse_question_id)
    return question_tree


def rec_question_tree(question, question_type, collapse_id):
    all_questions = [content for content in load_form_contents().get('codes')]

    if not question_type:
        return question

    elif question_type == "question-binary":
        try:
            code_yes = str.split(question.get("next_yes"), '=')[1]
        except IndexError:
            question['id'] = str(uuid.uuid4())
            question['collapse_id'] = collapse_id
            question['question_type'] = question_type
            return question

        question_yes = [match for match in all_questions if match.get('code') == code_yes][0]
        question_yes_type = find_question_type(question_yes)

        rec_question_tree(question_yes, question_yes_type, random.randint(10, 10000) + collapse_id)
        question['id'] = str(uuid.uuid4())
        question['question_type'] = question_type
        question['next_yes'] = question_yes
        question['collapse_id'] = collapse_id

        try:
            code_no = str.split(question.get("next_no"), '=')[1]
        except IndexError:
            question['id'] = str(uuid.uuid4())
            question['collapse_id'] = collapse_id
            question['question_type'] = question_type
            return question

        question_no = [match for match in all_questions if match.get('code') == code_no][0]
        question_no_type = find_question_type(question_no)

        rec_question_tree(question_no, question_no_type, random.randint(10, 10000) + collapse_id)
        question['id'] = str(uuid.uuid4())
        question['question_type'] = question_type
        question['next_no'] = question_no
        question['collapse_id'] = collapse_id

    elif question_type == "question-options" or question_type == "question-input":
        try:
            next_code = str.split(question.get("next"), '=')[1]
        except IndexError:
            question['id'] = str(uuid.uuid4())
            question['collapse_id'] = collapse_id
            question['question_type'] = question_type
            return question

        next_question = [match for match in all_questions if match.get('code') == next_code][0]
        next_question_type = find_question_type(next_question)

        rec_question_tree(next_question, next_question_type, collapse_id)
        question['id'] = str(uuid.uuid4())
        question['question_type'] = question_type
        question['next'] = next_question
        question['collapse_id'] = collapse_id

    else:

        print('type not found')

    return question


def track_answer_branch(question_answer_pairs, all_questions):
    answer_codes = []
    for pair in question_answer_pairs:

        for question in all_questions["codes"]:

            if len(answer_codes) < 1:
                answer_codes.append(pair["question"])

            if answer_codes[-1] == question["code"] and pair["question"] == question["code"]:

                if find_question_type(question) == "question-binary":

                    if pair["answer"] == "Ja":
                        try:
                            answer_codes.append(question["next_yes"].split("=")[1])
                            break
                        except IndexError:
                            # /acquisition
                            continue

                    elif pair["answer"] == "Nein":
                        try:
                            answer_codes.append(question["next_no"].split("=")[1])
                            break
                        except IndexError:
                            # /acquisition
                            continue
                    else:
                        pass

                else:
                    try:
                        answer_codes.append(question["next"].split("=")[1])
                        break
                    except IndexError:
                        # /acquisition
                        continue

    return answer_codes
