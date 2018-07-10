import tornado.web

from poc_services.advanced_view_service import build_questions_tree


class AdvancedViewController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):

        self.render(
            "advanced-interview.html",
            question_tree=build_questions_tree()
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
