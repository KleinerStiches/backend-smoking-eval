import tornado.web

from poc_models.forminfo import QuestionInputFormInfo

from poc_storage.handling_json import load_dictionary, dump_dictionary, load_form_contents


class InputQuestionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        code = self.get_query_argument("code")

        view_contents = load_form_contents()

        for content in view_contents["codes"]:
            if content["code"] == code:
                form_info = QuestionInputFormInfo(
                    question=content.get("question"),
                    placeholder=content.get("placeholder"),
                    redirect_next=content.get("next")
                )

        self.render(
            "input_question.html",
            question=form_info.question,
            question_code=code,
            input_placeholder=form_info.placeholder,
            redirect_next=form_info.next
        )

    def post(self, *args, **kwargs):
        redirection = self.get_body_argument(name="redirect_next")

        questionary = load_dictionary()
        question_code = self.get_body_argument(name="question_code")
        questionary[question_code] = self.get_body_argument(name="answer")
        dump_dictionary(questionary)

        self.redirect("{}".format(redirection))

