import pytest
import time

from data.data_urls import BROWSER_WINDOWS_URL
from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestBrowserWindowsPage:

    def test_verify_status_code_after_click_btn_new_tab(self, driver):
        browser_win = BrowserWindowsPage(driver, BROWSER_WINDOWS_URL)
        browser_win.open()
        browser_win.click_btn_new_tab()
        link = browser_win.get_link_in_the_new_tab()
        status_code = browser_win.get_status_code(link)
        assert status_code == "200", f"Status code is {status_code}"
