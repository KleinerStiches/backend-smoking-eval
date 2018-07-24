from poc_storage.handling_json import load_dictionary, dump_dictionary, load_form_contents


def load_summary(current_question_code):
    answers = load_dictionary()
    form_contents = load_form_contents()

    for content in form_contents["codes"]:
        question_specific_url = find_questions_url(content)
        content["question_url"] = question_specific_url

    answer_summary = [
        {
            "code": key,
            "question": content.get("question"),
            "answer": answers.get(key),
            "question_url": content.get("question_url")
        }
        for content in form_contents["codes"]
        for key in answers
        if content["code"] == key
    ]

    # if the current question is not in the answers append the current question to the summary
    if not [answer for answer in answer_summary if answer['code'] == current_question_code]:
        answer_summary.append(
            [
                {
                    "code": current_question_code,
                    "question": content.get("question"),
                    "answer": "",
                    "question_url": content.get("question_url")
                }
                for content in form_contents["codes"]
                if content["code"] == current_question_code
            ][0]
        )

    return answer_summary



def find_questions_url(question_form_info):
    key_map = {
        "next_yes": "question-binary?code=",
        "placeholder": "question-input?code=",
        "options": "question-options?code="
    }

    for key in question_form_info:
        if key in key_map:
            return key_map.get(key)

