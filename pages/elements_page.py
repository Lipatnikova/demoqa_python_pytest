from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def get_placeholder_full_name(self):
        return self.get_placeholder(self.locators.FULL_NAME)

    def get_placeholder_email(self):
        return self.get_placeholder(self.locators.EMAIL)

    def get_placeholder_current_address(self):
        return self.get_placeholder(self.locators.CURRENT_ADDRESS)

    def get_placeholder_permanent_address(self):
        return self.get_placeholder(self.locators.PERMANENT_ADDRESS)

