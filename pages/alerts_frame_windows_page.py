from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators as locators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    def click_btn_new_tab(self):
        self.click_button(locators.NEW_TAB_BTN)

    def click_btn_new_window(self):
        self.click_button(locators.NEW_WINDOW_BTN)

    def click_btn_new_window_msg(self):
        self.click_button(locators.NEW_WINDOW_MESSAGE_BTN)

    def get_link_in_the_new_tab(self):
        self.switch_to_the_second_window()
        return self.get_actual_url_of_current_page()
