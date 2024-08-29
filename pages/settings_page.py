from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):
    SETTINGS_OPTION = (By.CSS_SELECTOR, 'div[class="menu_block_1"] a[href="/settings"]') #//a[@href='/settings']
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, "a[href='/profile-edit']")



    def click_settings_option(self):
        sleep(3)
        self.driver.find_element(*self.SETTINGS_OPTION).click()
        # self.wait_and_click(*self.SETTINGS_OPTION)
        # sleep(6)
        # self.click(*self.SETTINGS_OPTION)


    def click_edit_profile_btn(self):
        self.click(*self.EDIT_PROFILE_BTN)
        sleep(6)




