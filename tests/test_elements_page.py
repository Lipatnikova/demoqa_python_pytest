import time

import pytest
from pages.elements_page import TextBoxPage
from data.data_urls import TEXT_BOX_URL


class TestElements:
    class TestTextBox:

        def test_compare_full_name_with_generated_below(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            full_name = text_box_page.fill_full_name()
            text_box_page.fill_email()
            text_box_page.fill_current_address()
            text_box_page.fill_permanent_address()
            text_box_page.click_submit()
            new_full_name = text_box_page.get_text_new_full_name()
            assert full_name == new_full_name, \
                "The Full Name in the field and the new Full Name generated below do not match"

        def test_compare_email_with_generated_below(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            text_box_page.fill_full_name()
            email = text_box_page.fill_email()
            text_box_page.fill_current_address()
            text_box_page.fill_permanent_address()
            text_box_page.click_submit()
            new_email = text_box_page.get_text_new_email()
            assert email == new_email, \
                "The Email in the field and the new Email generated below do not match"

        def test_compare_current_address_with_generated_below(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            text_box_page.fill_full_name()
            text_box_page.fill_email()
            current_address = text_box_page.fill_current_address()
            text_box_page.fill_permanent_address()
            text_box_page.click_submit()
            new_current_address = text_box_page.get_text_new_current_address()
            assert current_address == new_current_address, \
                "The Current Address in the field and the new Current Address generated below do not match"

        def test_compare_permanent_address_with_generated_below(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            text_box_page.fill_full_name()
            text_box_page.fill_email()
            text_box_page.fill_current_address()
            permanent_address = text_box_page.fill_permanent_address()
            text_box_page.click_submit()
            new_permanent_address = text_box_page.get_text_new_permanent_address()
            assert permanent_address == new_permanent_address, \
                "The Permanent Address in the field and the new Current Address generated below do not match"

        def test_verify_correct_email(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            email = text_box_page.fill_email()
            text_box_page.is_valid_email(email)
            assert text_box_page.is_valid_email(email), "Invalid email"

        @pytest.mark.parametrize('email', ["   ", "12313123", "AsRhf", "@dfdgd", ".com"])
        def test_verify_incorrect_email(self, driver, email):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            text_box_page.fill_incorrect_email(email)
            text_box_page.is_valid_email(email)
            assert text_box_page.is_valid_email(email) is False, "Invalid email"

        def test_verify_placeholder_full_name(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            assert text_box_page.get_placeholder_full_name() == "Full Name", \
                "Can not find placeholder Full Name"

        def test_verify_placeholder_email(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            assert text_box_page.get_placeholder_email() == "name@example.com", \
                "Can not find placeholder Email"

        def test_verify_placeholder_current_address(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            assert text_box_page.get_placeholder_current_address() == "Current Address", \
                "Can not find placeholder Current Address"

        @pytest.mark.xfail
        def test_verify_placeholder_permanent_address(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            assert text_box_page.get_placeholder_permanent_address() == "Permanent Address", \
                "Can not find placeholder Permanent Address"
