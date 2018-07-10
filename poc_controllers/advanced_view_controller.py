import tornado.web

from poc_services.advanced_view_service import find_question_type
from poc_storage.handling_json import load_form_contents


class AdvancedViewController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):

        # TODO get current question if not none
        # /advanced-interview?code=[q_code]&next=[next_yes/next_no]
        code = self.get_argument(name="code")
        next = self.get_argument(name="next")

        # TODO get all the answered questions
        view_contents = load_form_contents()

        # TODO check the currents question type
        # if is binary return the question
        # dig next until type is binary or /acquisition

        # return the answered questions to render

        # return the open question/s

        for content in view_contents["codes"]:
            question_specific_url = find_question_type(content)
            content["question_type"] = question_specific_url

        self.render(
            "advanced-interview.html",
            questions=[content for content in view_contents["codes"]]
        )

    # def post(self, *args, **kwargs):
    #     pass
    # answer = self.get_body_argument(name="answer")
    #
    # update_questionary(
    #     key=self.get_body_argument(name="question_code"),
    #     value=answer
    # )
    #
    # if answer == "Ja":
    #     redirection = self.get_body_argument(name="next_yes")
    # elif answer == "Nein":
    #     redirection = self.get_body_argument(name="next_no")
    # else:
    #     redirection = "/home"
    #
    # self.redirect("{}".format(redirection))
