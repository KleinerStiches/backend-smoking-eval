import tornado.web
from tornado.web import MissingArgumentError

from poc_services.advanced_view_service import build_questions_tree
from poc_storage.handling_json import load_form_contents
from poc_services.questionary_service import update_questionary


class AdvancedViewController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):

        self.render(
            "advanced-interview.html",
            question_tree=build_questions_tree()
        )

    def post(self, *args, **kwargs):
        all_questions = load_form_contents()

        question_answer_pairs = []
        for current_question in all_questions["codes"]:
            try:
                question_answer_pairs.append(
                    {
                        "question": current_question["code"],
                        "answer": self.get_body_argument("answer-{}".format(
                            str(current_question["code"])
                        ))
                    }
                )
            except MissingArgumentError:
                continue

        for pair in question_answer_pairs:
            if pair["answer"]:
                update_questionary(
                    key=pair["question"],
                    value=pair["answer"]
                )

        redirection = "/acquisition"
        self.redirect("{}".format(redirection))
