import tornado.web


class AcquisitionController(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        self.render("acquisition.html")
