import tornado.web
import regex
from tornado.web import MissingArgumentError

from poc_services.advanced_view_service import build_questions_tree, \
    find_question_type, track_answer_branch
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
                question_type = find_question_type(current_question)
                question_answer_pairs.append(
                    {
                        "question": current_question["code"],
                        "type": question_type,
                        "answer": self.get_body_argument(
                            "answer-{0}".format(str(current_question["code"]))
                        )
                    }
                )
            except MissingArgumentError:
                continue

        # TODO instead of this code below here try realise the first TODO in the TODO of smoking eval
        # TODO problem with the solution below is that when multiple same codes were answered not the correct ones
        # TODO can be displayed
        # get the answers from the completely answered question branch
        # answer_codes = track_answer_branch(
        #     question_answer_pairs,
        #     all_questions
        # )

        # store only answers from the complete answer branch
        for pair in question_answer_pairs:
            # if pair["answer"] and pair["question"] in answer_codes:
                update_questionary(
                    key=pair["question"],
                    value=pair["answer"]
                )

        redirection = "/acquisition"
        self.redirect("{}".format(redirection))
