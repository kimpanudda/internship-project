from selenium.webdriver.common.by import By
from pages.base_page import Page



class SettingsPage(Page):
    SETTINGS_OPTION = (By.CSS_SELECTOR, "div[class='menu_block_1'] a[href='/settings']")
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "a[href='/profile-edit']")



    def click_settings_option(self):
        self.wait_and_click(*self.SETTINGS_OPTION)



    def click_edit_profile_btn(self):
        self.wait_and_click(*self.EDIT_PROFILE_BTN)





