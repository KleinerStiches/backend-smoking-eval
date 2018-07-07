
import tornado.web


class Header(tornado.web.UIModule):
    def render(self):

        return self.render_string(
            "partials/header.html")


class Footer(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "partials/footer.html")


class Summary(tornado.web.UIModule):
    def render(self, summary):
        return self.render_string(
            "partials/summary.html",
            summary=summary
        )
