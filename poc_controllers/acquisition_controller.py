import tornado.web

from poc_services.questionary_service import clear_questionary
from poc_services.summary_service import load_summary


class AcquisitionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render(
            "acquisition.html",
            summary=load_summary()
        )

    def post(self, *args, **kwargs):
        clear_questionary()
        self.redirect("/home")



