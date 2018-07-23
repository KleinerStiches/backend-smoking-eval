import tornado.web

from poc_services.questionary_service import clear_questionary


class AcquisitionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render("acquisition.html")

    def post(self, *args, **kwargs):
        clear_questionary()
        self.redirect("/home")



