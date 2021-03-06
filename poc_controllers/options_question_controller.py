import tornado.web

from poc_services.summary_service import load_summary
from poc_services.questionary_service import update_questionary, questionary_contains_answer
from poc_models.forminfo import QuestionOptionsFormInfo
from poc_storage.handling_json import load_form_contents


class OptionsQuestionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        code = self.get_query_argument("code")

        view_contents = load_form_contents()

        for content in view_contents["codes"]:
            if content["code"] == code:
                form_info = QuestionOptionsFormInfo(
                    question=content.get("question"),
                    options=content.get("options"),
                    redirect_next=content.get("next")
                )

        stored_answer = questionary_contains_answer(code)

        self.render(
            "options_question.html",
            question=form_info.question,
            question_code=code,
            options=form_info.options,
            redirect_next=form_info.next,
            summary=load_summary(code),
            answer=stored_answer
        )

    def post(self, *args, **kwargs):
        redirection = self.get_body_argument(name="redirect_next")

        update_questionary(
            key=self.get_body_argument(name="question_code"),
            value=self.get_body_argument(name="answer")
        )

        self.redirect("{}".format(redirection))

