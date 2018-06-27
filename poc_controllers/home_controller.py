import tornado.web


class HomeController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render("home.html")
