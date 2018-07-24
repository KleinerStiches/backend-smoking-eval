import tornado.web

from poc_services.summary_service import load_summary
from poc_services.questionary_service import update_questionary, \
    questionary_contains_answer, remove_answers_until
from poc_models.forminfo import QuestionBinaryFormInfo
from poc_storage.handling_json import load_form_contents


class BinaryQuestionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        code = self.get_query_argument("code")

        view_contents = load_form_contents()

        for content in view_contents["codes"]:
            if content["code"] == code:
                form_info = QuestionBinaryFormInfo(
                    question=content.get("question"),
                    next_yes=content.get("next_yes"),
                    next_no=content.get("next_no")
                )

        self.render(
            "binary_question.html",
            question=form_info.question,
            question_code=code,
            next_yes=form_info.next_yes,
            next_no=form_info.next_no,
            summary=load_summary()
        )

    def post(self, *args, **kwargs):
        answer = self.get_body_argument(name="answer")
        current_question_code = self.get_body_argument(name="question_code")

        # if the question was asked before and the answer changed
        # remove questionaries answers until this question
        current_question_answer = questionary_contains_answer(current_question_code)
        if current_question_answer != answer and current_question_answer:
            remove_answers_until(current_question_code)

        update_questionary(
            key=self.get_body_argument(name="question_code"),
            value=answer
        )

        if answer == "Ja":
            redirection = self.get_body_argument(name="next_yes")
        elif answer == "Nein":
            redirection = self.get_body_argument(name="next_no")
        else:
            redirection = "/home"

        self.redirect("{}".format(redirection))
