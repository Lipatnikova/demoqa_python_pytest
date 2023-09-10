from data.data_urls import MAIN_PAGE_URL
from pages.main_page import MainPage


class TestMainPage:

    def test_verify_url_main_page(self, driver):
        page = MainPage(driver, MAIN_PAGE_URL)
        page.open()
        actual_url = page.get_actual_url_of_current_page()
        assert actual_url == "https://demoqa.com/", \
            "Invalid url"

    def test_verify_title_main_page(self, driver):
        page = MainPage(driver, MAIN_PAGE_URL)
        page.open()
        actual_title = page.get_actual_title_of_current_page()
        assert actual_title == "DEMOQA", \
            f"Expected title page: 'DEMOQA', Actual title page: {actual_title}"

