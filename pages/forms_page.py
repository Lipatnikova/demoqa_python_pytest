import random

from generator.generator import get_person
from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators as Form
from selenium.webdriver.support.ui import Select


class FormsPage(BasePage):
    def fill_first_name(self):
        info = next(get_person())
        first_name = info.first_name
        self.send_keys_in_field(Form.FIRST_NAME, first_name)
        return first_name

    def fill_last_name(self):
        info = next(get_person())
        last_name = info.last_name
        self.send_keys_in_field(Form.LAST_NAME, last_name)
        return last_name

    def fill_email(self):
        info = next(get_person())
        email = info.email
        self.send_keys_in_field(Form.EMAIL, email)
        return email

    def choose_gender(self):
        locator = Form.GENDER
        gender_click = self.click_button(locator)
        gender_text = self.get_text(locator)
        return gender_text

    def fill_mobile_number(self):
        info = next(get_person())
        mobile = info.mobile
        self.send_keys_in_field(Form.PHONE_NUMBER, mobile)
        return mobile

    def choose_date_of_birth(self):
        calender = self.element_is_visible(Form.BIRTH_DAY)
        calender.click()
        # Select year:
        self.click_button(Form.YEARS_CHANGE)
        year_change = self.element_is_visible(Form.YEARS)
        year = year_change.text
        year_change.click()
        # Select month:
        self.element_is_visible(Form.MONTHS_CHANGE).click()
        month_change = self.element_is_visible(Form.MONTHS)
        month = month_change.text
        month_change.click()
        # Select day:
        week = self.elements_are_present(Form.DAY_DATE_PICKER)
        random_day = random.choice(week)
        day = random_day.text
        random_day.click()
        return day, month, year

    def fill_subjects(self):
        pass

    def choose_hobbies(self):
        pass

    def select_picture(self):
        pass

    def fill_current_address(self):
        pass

    def select_state(self):
        pass

    def select_city(self):
        pass

    def click_submit(self):
        pass
