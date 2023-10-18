import pytest

from data.data import AlertsData, FramesData, ModalData
from data.data_urls import BROWSER_WINDOWS_URL, ALERTS_URL, FRAMES_URL, NESTED_FRAMES_URL, MODAL_DIALOGS_URL
from generator.generator import random_num
from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators


class TestBrowserWindowsPage:

    def test_verify_status_code_after_click_btn_new_tab(self, driver):
        browser_win = BrowserWindowsPage(driver, BROWSER_WINDOWS_URL)
        browser_win.open()
        browser_win.click_btn_new_tab()
        link = browser_win.get_link_in_the_new_tab()
        status_code = browser_win.get_status_code(link)
        assert status_code == "200", f"Status code is {status_code}"

    @pytest.mark.parametrize('locator_btn', BrowserWindowsPageLocators.BTNS_FOR_CLICK)
    def test_verify_count_opened_new_windows(self, driver, locator_btn):
        browser_win = BrowserWindowsPage(driver, BROWSER_WINDOWS_URL)
        browser_win.open()
        count_clicks = random_num()
        for i in range(1, count_clicks):
            browser_win.click_button(locator_btn)
            browser_win.switch_to_the_x_window(0)
        count_windows = browser_win.get_count_windows()
        assert count_windows == count_clicks, \
            "The count of new tabs or windows opened does not correspond to the count of button clicks"

    @pytest.mark.parametrize('locator_btn', BrowserWindowsPageLocators.BTNS_FOR_CLICK)
    def test_verify_urls_new_windows(self, driver, locator_btn):
        browser_win = BrowserWindowsPage(driver, BROWSER_WINDOWS_URL)
        browser_win.open()
        count_clicks = random_num()
        for i in range(1, count_clicks):
            browser_win.click_button(locator_btn)
            browser_win.switch_to_the_x_window(i)
            assert browser_win.get_actual_url_of_current_page() == "https://demoqa.com/sample"
            browser_win.switch_to_the_x_window(0)

    @pytest.mark.parametrize('locator_btn', BrowserWindowsPageLocators.BTNS_FOR_CLICK)
    def test_verify_in_new_window_text(self, driver, locator_btn):
        browser_win = BrowserWindowsPage(driver, BROWSER_WINDOWS_URL)
        browser_win.open()
        browser_win.click_button(locator_btn)
        browser_win.switch_to_the_x_window(1)
        text = browser_win.get_heading_text_in_new_window()
        assert text == "This is a sample page", "The text in the new tab is incorrect"


class TestAlertsPage:

    def test_verify_text_in_alert(self, driver):
        alert_page = AlertsPage(driver, ALERTS_URL)
        alert_page.open()
        alert_page.click_btn_see_alert()
        text = alert_page.get_alert_text()
        assert text == "You clicked a button", \
            "The alert doesn't contain expected text"

    def test_verify_text_in_alert_after_five_seconds(self, driver):
        alert_page = AlertsPage(driver, ALERTS_URL)
        alert_page.open()
        alert_page.click_btn_see_alert_will_appear_after_five_seconds()
        alert_page.alert_is_present()
        text = alert_page.get_alert_text()
        assert text == "This alert appeared after 5 seconds", \
            "The alert doesn't contain expected text"

    @pytest.mark.parametrize('item', AlertsData.BTN_IN_ALERT)
    def test_verify_text_in_alert_confirm_box_will_appear(self, driver, item):
        alert_page = AlertsPage(driver, ALERTS_URL)
        alert_page.open()
        alert_page.click_btn_confirm_box_will_appear()
        text_btn_alert = alert_page.complex_alert(item)
        text_result = alert_page.get_text_result_after_click_confirm_in_alert()
        assert text_btn_alert in text_result, \
            "The text result after click button doesn't contain expected text"

    def test_verify_text_in_alert_prompt_box_will_appear(self, driver):
        alert_page = AlertsPage(driver, ALERTS_URL)
        alert_page.open()
        alert_page.click_btn_prompt_box_will_appear()
        alert_page.alert_is_present()
        text_add_to_alert = alert_page.prompt_alert()
        text_result = alert_page.get_text_result_after_click_prompt_in_alert()
        assert text_add_to_alert in text_result, \
            "The text result after click button doesn't contain expected text"


class TestFramesPage:

    def test_count_frames_on_the_page(self, driver):
        frames_page = FramesPage(driver, FRAMES_URL)
        frames_page.open()
        frames_page.first_frame_is_present()
        count_frames = frames_page.get_count_frames_on_the_page()
        assert count_frames == 2, "Incorrect count of frames on the page"

    @pytest.mark.parametrize("item", FramesData.SIZE_FRAME)
    def test_verify_frames_options(self, driver, item):
        frame_page = FramesPage(driver, FRAMES_URL)
        frame_page.open()
        result = frame_page.get_frame_info(item)
        assert result == ['500px', '350px', 'This is a sample page'] or \
               result == ['100px', '100px', 'This is a sample page'], "The frame does not exist"


class TestNestedFramesPage:
    def test_nested_frames(self, driver):
        nested_frame_page = NestedFramesPage(driver, NESTED_FRAMES_URL)
        nested_frame_page.open()
        text_first_frame = nested_frame_page.nested_frame_page_text_first_frame()
        text_second_frame = nested_frame_page.nested_frame_page_text_second_frame()
        assert text_first_frame == "Parent frame", "Parent frame doesn't exist or does not contain the expected text"
        assert text_second_frame == "Child Iframe", "Child frame doesn't exist or does not contain the expected text"


class TestModalDialogsPage:

    def test_verify_button_small_modal_text(self, driver):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        text = modal_page.get_text_small_modal_btn()
        assert text == "Small modal", "The button hasn't expected text"

    def test_verify_button_large_modal_text(self, driver):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        text = modal_page.get_text_large_modal_btn()
        assert text == "Large modal", "The button hasn't expected text"

    def test_verify_content_small_modal(self, driver):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        modal_page.click_btn_small_modal()
        header, title = modal_page.get_content_from_modal()
        assert header == "Small Modal", "Modal hasn't header expected text"
        assert title == "This is a small modal. It has very less content", \
            "The Modal hasn't expected text"

    def test_verify_content_large_modal(self, driver):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        modal_page.click_btn_large_modal()
        header, title = modal_page.get_content_from_modal()
        assert header == "Large Modal", "Modal hasn't header expected text"
        assert len(title) > 100, "Modal hasn't title text"

    @pytest.mark.parametrize('close', ModalData.CLOSE_MODAL)
    def test_check_close_small_modal_different_ways(self, driver, close):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        modal_page.click_btn_small_modal()
        button = modal_page.close_small_modal_different_ways(close)
        assert close in button, f"Didn't click on the {close}"

    @pytest.mark.parametrize('close', ModalData.CLOSE_MODAL)
    def test_check_close_large_modal_different_ways(self, driver, close):
        modal_page = ModalDialogsPage(driver, MODAL_DIALOGS_URL)
        modal_page.open()
        modal_page.click_btn_small_modal()
        button = modal_page.close_large_modal_different_ways(close)
        assert close in button, f"Didn't click on the {close}"
