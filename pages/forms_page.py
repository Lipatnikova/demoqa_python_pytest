import random
import os

from generator.generator import get_person, generated_subject, generated_file, generated_city
from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators as Form
from selenium.webdriver import Keys
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
        return mobile[:10]

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
        subject_list = generated_subject()
        for item in subject_list:
            self.element_is_visible(Form.SUBJECT).send_keys(item)
            self.element_is_visible(Form.SUBJECT).send_keys(Keys.RETURN)

    def choose_hobbies(self):
        locator = Form.HOBBIES
        hobby = self.click_button(locator)
        return self.get_text(locator)

    def select_picture(self):
        file_name, path = generated_file()
        self.element_is_visible(Form.FILE_INPUT).send_keys(path)
        os.remove(path)
        return file_name.split('\\')[-1]

    def fill_current_address_and_select_state_and_city(self):
        info = next(get_person())
        current_address = info.current_address
        self.send_keys_in_field(Form.PHONE_NUMBER, current_address)
        state, city = generated_city()
        new_city = city[random.randint(0, len(city) - 1)]
        self.element_is_visible(Form.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(Form.SELECT_STATE).click()
        self.element_is_visible(Form.STATE_INPUT).send_keys(state)
        self.element_is_visible(Form.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(Form.SELECT_CITY).click()
        self.element_is_visible(Form.CITY_INPUT).send_keys(new_city)
        self.element_is_visible(Form.CITY_INPUT).send_keys(Keys.RETURN)
        return current_address, state, new_city

    def click_submit(self):
        # self.click_button(Form.SUBMIT)
        self.element_is_visible(Form.SUBMIT).send_keys(Keys.RETURN)

    def return_correct_form(self, data):
        text1 = []
        second = data.split('\n')[1:]
        for i in second:
            if "Name" in i:
                a = i.split()[2:]
                text1.append(a)
            elif "Email" in i:
                a = i.split()[2:]
                text1.append(a)
            elif "Gender" in i:
                a = i.split()[1:]
                text1.append(a)
            elif "Date" in i:
                a = i.replace(',', ' ').split()[3:]
                text1.append(a)
            elif "Mobile" in i:
                a = i.split()[1:]
                text1.append(a)
            elif "Hobbies" in i:
                a = i.split()[1:]
                text1.append(a)
            elif "Picture" in i:
                a = i.split()[1:]
                text1.append(a)
            elif "Address" in i:
                a = [' '.join(i.split()[1:])]
                text1.append(a)
            elif "State" in i:
                a = i.split()[3:]
                text1.append(a)
        return text1

    def form_result(self):
        result_list = self.elements_are_visible(Form.ALL_TABLE)
        data = ""
        for item in result_list:
            self.go_to_element(item)
            data += item.text
        print(data)
        correct_result = self.return_correct_form(data)
        return correct_result
