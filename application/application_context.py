import tornado.ioloop
import tornado.web

#import ui templates
from view import partials

# import controllers
from poc_controllers.binary_question_controller import BinaryQuestionController
from poc_controllers.options_question_controller import OptionsQuestionController
from poc_controllers.input_question_controller import InputQuestionController
from poc_controllers.register_controller import RegisterController
from poc_controllers.home_controller import HomeController
from poc_controllers.acquisition_controller import AcquisitionController

from pathlib import Path


base_path = Path(__file__).parents[2]


class ApplicationContext(tornado.web.Application):

    def __init__(self):

        handlers = [

            (r"/", HomeController),
            (r"/home", HomeController),
            (r"/acquisition", AcquisitionController),
            (r"/register", RegisterController),
            (r"/question-binary", BinaryQuestionController),
            (r"/question-options", OptionsQuestionController),
            (r"/question-input", InputQuestionController)
            ]

        settings = dict(
            ui_modules=partials,
            template_path='{}\\smoking_eval'.format(base_path),
            static_path='{}\\smoking_eval/'.format(base_path)
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        # TODO source out the connection information to a separate resource file
        # self.db_uri = "mongodb://localhost:27017/issue_manager"
        # self.connection_alias = "issue-manager-con"
        #
        # # create a connection manager and set up the connection
        # mongo_con = MongoConnectionManager()
        # mongo_con.generate_connection(mongodb_connection_uri=self.db_uri, connection_alias=self.connection_alias)

