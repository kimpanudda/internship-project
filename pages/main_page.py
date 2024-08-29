from pages.base_page import Page


class MainPage(Page):

    def open(self):
        self.open_url('https://soft.reelly.io/')