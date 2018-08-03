import tornado.web

from poc_services.questionary_service import clear_questionary


class HomeController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        clear_questionary()
        self.render("home.html")
