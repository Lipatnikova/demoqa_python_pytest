from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def test(self):
        pass
