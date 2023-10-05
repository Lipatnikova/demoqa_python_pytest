import pytest

from data.data_urls import BROWSER_WINDOWS_URL
from generator.generator import random_num
from pages.alerts_frame_windows_page import BrowserWindowsPage
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
