import pytest
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, ButtonsPage, LinksPage, BrokenLinksImage, \
    UploadAndDownload, DynamicPropertiesPage, WebTablesPage
from data.data_urls import TEXT_BOX_URL, CHECK_BOX_URL, RADIO_BUTTON_URL, BUTTONS_URL, LINKS_URL, MAIN_PAGE_URL, \
    BROKEN_LINKS_URL, UPLOAD_AND_DOWNLOAD_URL, DYNAMIC_PROPERTIES_URL, WEB_TABLES_URL
from data.data import LinksAndUrls
from generator.generator import random_num
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import LinksPageLocators
from locators.elements_page_locators import BrokenLinksImageLocators


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

        @pytest.mark.parametrize('field', TextBoxPageLocators.FIELDS)
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

        def test_add_new_person_in_the_table(self, driver):
            web_tables_page = WebTablesPage(driver, WEB_TABLES_URL)
            web_tables_page.open()
            for i in range(1, random_num()):
                web_tables_page.click_btn_add()
                new_person = web_tables_page.fill_registration_form()
                web_tables_page.click_btn_submit()
                result = web_tables_page.get_row_new_added_person()
                assert new_person in result, "A new person is not in the table"

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
            cursor_before, cursor_after = buttons_page.cursor_button_double_click()
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

    class TestLinksPage:
        @pytest.mark.parametrize('link', LinksPageLocators.HOMES_LINKS)
        def test_switch_between_opened_windows_after_click_home_links(self, driver, link):
            links_page = LinksPage(driver, LINKS_URL)
            links_page.open()
            links_page.click_link(link)
            assert links_page.count_opened_windows() == 2, \
                "After click link the second window is not revealed."

        @pytest.mark.parametrize('link', LinksPageLocators.HOMES_LINKS)
        def test_verify_home_links_href(self, driver, link):
            links_page = LinksPage(driver, LINKS_URL)
            links_page.open()
            actual_href = links_page.get_link_href(link)
            assert actual_href == MAIN_PAGE_URL, \
                "The link is broken or url is incorrect"

        @pytest.mark.parametrize("link, url", LinksAndUrls.LINKS_AND_URLS)
        def test_check_all_links(self, driver, link, url):
            link_page = LinksPage(driver, "https://demoqa.com/links")
            link_page.open()
            link_page.click_link(link)
            msg = link_page.text_msg_after_click()
            status_code = link_page.get_status_code(url)
            assert status_code in msg, f"Wrong status code. Actual code:{status_code}, expected code:{msg}"

    class TestBrokenLinksImage:
        @pytest.mark.xfail("The second image is broken")
        @pytest.mark.parametrize('img', BrokenLinksImageLocators.IMG)
        def test_verify_image_is_displayed(self, driver, img):
            broken_links_img_page = BrokenLinksImage(driver, BROKEN_LINKS_URL)
            broken_links_img_page.open()
            assert broken_links_img_page.img_is_displayed(img), \
                "The image is not correct"

        @pytest.mark.xfail("The second link is broken")
        @pytest.mark.parametrize('link', BrokenLinksImageLocators.LINKS)
        def test_verify_links(self, driver, link):
            broken_links_img_page = BrokenLinksImage(driver, BROKEN_LINKS_URL)
            broken_links_img_page.open()
            url = broken_links_img_page.get_href(link)
            status_code = broken_links_img_page.get_status_code(url)
            assert status_code == '200', \
                f"The link doesn't work. The status code is {status_code}."

    class TestUploadAndDownloadPage:
        def test_download_file(self, driver):
            download_page = UploadAndDownload(driver, UPLOAD_AND_DOWNLOAD_URL)
            download_page.open()
            check = download_page.download_file()
            assert check is True, "The downloaded file is not a image"

        def test_upload_file(self, driver):
            upload_file = UploadAndDownload(driver, UPLOAD_AND_DOWNLOAD_URL)
            upload_file.open()
            file_name, result = upload_file.upload_file()
            assert file_name == result, "There is not been upload"

    class TestDynamicPropertiesPage:

        def test_verify_random_id_in_text(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, DYNAMIC_PROPERTIES_URL)
            dynamic_properties.open()
            id_1 = dynamic_properties.get_text_random_id()
            dynamic_properties.refresh_page()
            id_2 = dynamic_properties.get_text_random_id()
            assert id_1 != id_2, "The ID has not changed after updating the page"

        def test_verify_btn_is_enable_after_five_seconds(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, DYNAMIC_PROPERTIES_URL)
            dynamic_properties.open()
            return dynamic_properties.verify_element_is_enable(), "The button is not enable"

        @pytest.mark.xfail("color_before поздно считывается")
        def test_verify_changed_of_color_in_btn(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, DYNAMIC_PROPERTIES_URL)
            dynamic_properties.open()
            color_before = dynamic_properties.get_color_text()
            time.sleep(6)
            color_after = dynamic_properties.get_color_text()
            assert color_after != color_before, "The color is not changed"

        def test_verify_is_not_visible_btn(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, DYNAMIC_PROPERTIES_URL)
            dynamic_properties.open()
            assert dynamic_properties.verify_btn_is_not_visible() is True, "The button don't appear"
