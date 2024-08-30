from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class LogInPage(Page):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, ".login-button.w-button")
    EMAIL = 'qaautomation@gmail.com'
    PASSWORD = 'testQA'



    def open_log_in_url(self):
        self.driver.get('https://soft.reelly.io/sign-in')


    def enter_email(self):
        self.input_text(self.EMAIL,*self.EMAIL_FIELD)


    def enter_password(self):
        self.input_text(self.PASSWORD,*self.PASSWORD_FIELD)


    def click_login_button(self):
        self.click(*self.LOGIN_BTN)
        sleep(6)



