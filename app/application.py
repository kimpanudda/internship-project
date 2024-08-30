from pages.base_page import Page
from pages.log_in_page import LogInPage
from pages.profile_page import ProfilePage
from pages.settings_page import SettingsPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.log_in_page = LogInPage(driver)
        self.settings_page = SettingsPage(driver)
        self.profile_page = ProfilePage(driver)