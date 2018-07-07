from poc_storage.handling_json import load_dictionary, dump_dictionary


relative_path = '\\smoking_eval\\store\\theme.json'


class ThemeService:

    def __init__(self, theme):
        self.theme = theme

    def update_theme(self, theme):
        dump_dictionary(eval_dictionary=theme, relative_path=relative_path)

    def select_theme(self):
        theme = load_dictionary(relative_path=relative_path)
        return theme
