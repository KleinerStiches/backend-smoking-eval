import json

from tornado.web import RequestHandler

from poc_storage.handling_json import load_dictionary, dump_dictionary


class RegisterController(RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render("register.html")

    def post(self, *args, **kwargs):
        questionary = load_dictionary()

        questionary["lastname"] = self.get_body_argument("lastname")
        questionary["firstname"] = self.get_body_argument("firstname")
        questionary["gender"] = self.get_body_argument("gender")
        questionary["date_of_birth"] = self.get_body_argument("date_of_birth")
        questionary["case_id"] = self.get_body_argument("case_id")

        dump_dictionary(eval_dictionary=questionary)

        questioning_type = self.get_body_argument(name="commit")

        if questioning_type == "Zum Fragen-Formular":
            self.redirect("/advanced-interview")
        elif questioning_type == "Zu den Fragen":
            self.redirect("/question-binary?code=3")
        else:
            self.redirect("/home")
