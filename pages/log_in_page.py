from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class LogInPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, ".login-button.w-button")



    def open_log_in_url(self):
        self.driver.get('https://soft.reelly.io/sign-in')


    def enter_email(self, email):
        self.input_text(email,*self.EMAIL_FIELD)


    def enter_password(self, password):
        self.input_text(password,*self.PASSWORD_FIELD)


    def click_login_button(self):
        self.click(*self.LOGIN_BTN)
        sleep(6)



