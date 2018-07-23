
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
    def render(self, summary, current_question_id):
        return self.render_string(
            "partials/summary.html",
            summary=summary,
            current_question_id=current_question_id
        )
