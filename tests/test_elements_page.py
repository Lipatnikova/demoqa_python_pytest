import pytest
import time
from pages.elements_page import TextBoxPage
from data.data_urls import TEXT_BOX_URL


class TestElements:
    class TestTextBox:

        def test_verify_field_full_name(self, driver):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            full_name = text_box_page.fill_full_name()
            text_box_page.fill_email()
            text_box_page.fill_current_address()
            text_box_page.fill_permanent_address()
            text_box_page.click_submit()
            new_full_name = text_box_page.get_text_new_full_name()
            assert full_name == new_full_name, "The full name is not correct"
            time.sleep(1)

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
