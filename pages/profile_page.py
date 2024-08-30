from selenium.webdriver.common.by import By
from pages.base_page import Page



class ProfilePage(Page):
    JOINED_COMPANY_FIELD = (By.ID, "When-joined-company-2")
    LANGUAGES_FIELD = (By.ID, "Languages")
    CLOSE_BTN = (By.CSS_SELECTOR, '.close-button.w-button')
    SAVE_BTN = (By.CSS_SELECTOR, '.save-changes-button')
    JOINED_COMPANY = '2024 Q3'
    LANGUAGES = 'English'


    def enter_test_info(self):
        # input text in the field
        self.input_text(self.JOINED_COMPANY, *self.JOINED_COMPANY_FIELD)
        self.input_text(self.LANGUAGES, *self.LANGUAGES_FIELD)


    def check_test_input(self):
        # verify text in the field
        self.verify_text(self.JOINED_COMPANY, *self.JOINED_COMPANY_FIELD)
        self.verify_text(self.LANGUAGES, *self.LANGUAGES_FIELD)


    def check_close_save_changes_buttons(self):
        self.wait_and_click(*self.CLOSE_BTN)
        self.wait_and_click(*self.SAVE_BTN)





