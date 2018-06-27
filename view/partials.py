
import tornado.web


class Header(tornado.web.UIModule):
    def render(self):

        return self.render_string(
            "partials/header.html")


class Footer(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "partials/footer.html")
