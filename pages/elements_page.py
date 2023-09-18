import random
import re
import requests

from PIL import Image, UnidentifiedImageError
from io import BytesIO
from generator.generator import get_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    ButtonsPageLocators, LinksPageLocators, BrokenLinksImageLocators


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

    def is_valid_email(self, email):
        """This method is validation Email field for correct email format"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
        valid_email = re.match(pattern, email)
        return valid_email is not None

    def fill_incorrect_email(self, email):
        self.send_keys_in_field(self.locators.EMAIL, email)

    def get_border_color_field(self, locator):
        return self.get_border_color(locator)

    def active_field(self, locator):
        self.element_is_visible(locator).click()

    def get_placeholder_full_name(self):
        return self.get_placeholder(self.locators.FULL_NAME)

    def get_placeholder_email(self):
        return self.get_placeholder(self.locators.EMAIL)

    def get_placeholder_current_address(self):
        return self.get_placeholder(self.locators.CURRENT_ADDRESS)

    def get_placeholder_permanent_address(self):
        return self.get_placeholder(self.locators.PERMANENT_ADDRESS)


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list_expand_button(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    def click_random_checkboxes(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 3
        while count != 0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_box(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        lst = []
        for i in checked_list:
            item = i.find_element("xpath", self.locators.TITLE_ITEM)
            lst.append(item.text)
        return str(lst).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT)
        lst = []
        for i in result_list:
            lst.append(i.text)
        return str(lst).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def title_question_text(self):
        return self.get_text(self.locators.TITLE_QUESTION)

    def click_random_radio_button(self, item):
        choices = {
            'Yes': self.locators.YES_BUTTON,
            'Impressive': self.locators.IMPRESSIVE_BUTTON,
            'No': self.locators.NO_BUTTON
        }
        click_button = self.element_is_visible(choices[item]).click()
        return click_button

    def get_text_message_result(self):
        return self.get_text(self.locators.OUTPUT_RESULT)


class WebTablesPage(BasePage):
    pass


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators

    def double_click(self):
        self.action_move_to_element_double_click(self.locators.DOUBLE_CLICK_BTN)

    def get_text_msg_about_double_click(self):
        return self.get_text(self.locators.MSG_DOUBLE)

    def cursor_button_double_click(self):
        """
        This method hovers the mouse cursor over the button
        and checks for the button cursor change
        """
        cursor_before = self.driver.execute_script("""return window.getComputedStyle(document.body).cursor;""")
        btn = self.element_is_visible(self.locators.DOUBLE_CLICK_BTN)
        self.action_move_to_element(btn)
        cursor_after = self.check_element_hover_style_using_js(btn, "cursor")
        return cursor_before, cursor_after

    def right_click(self):
        self.action_move_to_element_right_click(self.locators.RIGHT_CLICK_BTN)

    def get_text_msg_about_right_click(self):
        return self.get_text(self.locators.MSG_RIGHT)

    def click(self):
        self.action_move_to_element_click(self.locators.CLICK_ME_BUTTON_BTN)

    def get_text_msg_about_click(self):
        return self.get_text(self.locators.MSG_CLICK_ME)


class LinksPage(BasePage):
    locators = LinksPageLocators

    def click_link(self, link):
        self.element_is_visible(link).click()

    def count_opened_windows(self):
        handles = self.driver.window_handles
        return len(handles)

    def get_link_href(self, link):
        return self.get_href(link)

    def text_msg_after_click(self):
        return self.get_text(self.locators.TEXT_AFTER_CLICK)


class BrokenLinksImage(BasePage):
    locators = BrokenLinksImageLocators

    def img_is_displayed(self, locator):
        src = self.element_is_visible(locator).get_attribute('src')
        response = requests.get(src)
        try:
            img = Image.open(BytesIO(response.content))
            return img
        except UnidentifiedImageError:
            return "Is not image"
        except Exception:
            return "The image is broken"
