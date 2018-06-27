

class FormInfo:

    def __init__(self, question, buttons=None):
        self.question = question
        self.buttons = buttons


class QuestionBinaryFormInfo:

    def __init__(self, question, next_yes, next_no):
        self.question = question
        self.next_yes = next_yes
        self.next_no = next_no


class QuestionOptionsFormInfo:

    def __init__(self, question, options, redirect_next):
        self.question = question
        self.options = options
        self.next = redirect_next


class QuestionInputFormInfo:

    def __init__(self, question, placeholder, redirect_next):
        self.question = question
        self.placeholder = placeholder
        self.next = redirect_next

