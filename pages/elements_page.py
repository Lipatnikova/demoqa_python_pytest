from generator.generator import get_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_full_name(self):
        info = next(get_person())
        full_name = info.full_name
        self.send_keys_in_field(self.locators.FULL_NAME, full_name)
        return full_name

    def fill_email(self):
        info = next(get_person())
        email = info.email
        self.send_keys_in_field(self.locators.EMAIL, email)
        return email

    def fill_current_address(self):
        info = next(get_person())
        current_address = info.current_address
        self.send_keys_in_field(self.locators.CURRENT_ADDRESS, current_address)
        return current_address

    def fill_permanent_address(self):
        info = next(get_person())
        permanent_address = info.permanent_address
        self.send_keys_in_field(self.locators.PERMANENT_ADDRESS, permanent_address)
        return permanent_address

    def click_submit(self):
        self.click_button(self.locators.SUBMIT)

    def get_text_new_full_name(self):
        return self.get_text_split(self.locators.CREATED_FULL_NAME)

    def get_text_new_email(self):
        return self.get_text_split(self.locators.CREATED_EMAIL)

    def get_text_new_current_address(self):
        return self.get_text_split(self.locators.CREATED_CURRENT_ADDRESS)

    def get_text_new_permanent_address(self):
        return self.get_text_split(self.locators.CREATED_PERMANENT_ADDRESS)

    def get_placeholder_full_name(self):
        return self.get_placeholder(self.locators.FULL_NAME)

    def get_placeholder_email(self):
        return self.get_placeholder(self.locators.EMAIL)

    def get_placeholder_current_address(self):
        return self.get_placeholder(self.locators.CURRENT_ADDRESS)

    def get_placeholder_permanent_address(self):
        return self.get_placeholder(self.locators.PERMANENT_ADDRESS)
