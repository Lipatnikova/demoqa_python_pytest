import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, ButtonsPage
from data.data_urls import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL, BUTTONS_URL
from locators.elements_page_locators import TextBoxPageLocators as locator


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

        @pytest.mark.parametrize('field', [locator.FULL_NAME, locator.EMAIL, locator.CURRENT_ADDRESS,
                                           locator.PERMANENT_ADDRESS])
        def test_verify_border_color_of_the_field(self, driver, field):
            text_box_page = TextBoxPage(driver, TEXT_BOX_URL)
            text_box_page.open()
            border_before = text_box_page.get_border_color(field)
            text_box_page.active_field(field)
            border_after = text_box_page.get_border_color(field)
            assert border_before != border_after, \
                "Border color of the field has not changed after click"

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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, CHECK_BOX_URL)
            check_box_page.open()
            check_box_page.open_full_list_expand_button()
            check_box_page.click_random_checkboxes()
            input_checkbox = check_box_page.get_checked_box()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, "Input text and output checkbox is not equal"

    class TestRadioButton:
        def test_verify_title_question_is_display(self, driver):
            radio_button_page = RadioButtonPage(driver, RADIO_BUTTON_URL)
            radio_button_page.open()
            title_text = radio_button_page.title_question_text()
            for item in title_text:
                assert len(item) != 0, "Title question is not display correct"

        radio_buttons_list = ['Yes', 'Impressive', 'No']

        @pytest.mark.parametrize('item', radio_buttons_list)
        def test_click_radio_button_compare_text_in_message(self, driver, item):
            radio_button_page = RadioButtonPage(driver, RADIO_BUTTON_URL)
            radio_button_page.open()
            radio_button_page.click_random_radio_button(item)
            text_in_message = radio_button_page.get_text_message_result()
            assert text_in_message == item, \
                f"{item} radiobutton test is not the same"

    class TestWebTablesPage:
        pass

    class TestButtonsPage:

        def test_button_double_click(self, driver):
            buttons_page = ButtonsPage(driver, BUTTONS_URL)
            buttons_page.open()
            buttons_page.double_click()
            msg = buttons_page.get_text_msg_about_double_click()
            assert msg == "You have done a double click", \
                "Message about click is not correct"

        def test_button_hover_verify_cursor_double_click(self, driver):
            buttons_page = ButtonsPage(driver, BUTTONS_URL)
            buttons_page.open()
            cursor_before, cursor_after = buttons_page.cursor_button_double_click(driver)
            assert cursor_before != cursor_after, "Mouse cursor has not changed"

        def test_button_right_click(self, driver):
            buttons_page = ButtonsPage(driver, BUTTONS_URL)
            buttons_page.open()
            buttons_page.right_click()
            msg = buttons_page.get_text_msg_about_right_click()
            assert msg == "You have done a right click", \
                "Message about click is not correct"

        def test_button_click(self, driver):
            buttons_page = ButtonsPage(driver, BUTTONS_URL)
            buttons_page.open()
            buttons_page.click()
            msg = buttons_page.get_text_msg_about_click()
            assert msg == "You have done a dynamic click", \
                "Message about click is not correct"
