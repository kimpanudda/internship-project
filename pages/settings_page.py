from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SettingsPage(Page):
    # SETTINGS_OPTION = (By.CSS_SELECTOR, "div[class='menu_block_1'] a[href='/settings']")
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "a[href='/profile-edit']")
    MENU_BTN = (By.CSS_SELECTOR, "div[class='assistant-mobile'] a[href='/main-menu']")



    def click_settings_option(self):
        sleep(3)
        # self.wait_and_click(*self.SETTINGS_OPTION)
        # self.click(*self.SETTINGS_OPTION)
        self.wait_and_click(*self.MENU_BTN)
        # sleep(6)


    def click_edit_profile_btn(self):
        self.click(*self.EDIT_PROFILE_BTN)
        sleep(6)




