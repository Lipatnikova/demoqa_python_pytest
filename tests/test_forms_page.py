from pages.forms_page import FormsPage
from data.data_urls import PRACTICE_FORM_URL


class TestFormsPage:
    def test_verify_fill_form_field(self, driver):
        form_page = FormsPage(driver, PRACTICE_FORM_URL)
        form_page.open()
        form_page.fill_first_name()
        form_page.fill_last_name()
        form_page.fill_email()
        form_page.choose_gender()
        form_page.fill_mobile_number()
        form_page.choose_date_of_birth()
        form_page.fill_subjects()
        form_page.choose_hobbies()
        form_page.select_picture()
        form_page.fill_current_address()
        form_page.select_state()
        form_page.select_city()
        form_page.click_submit()
        # assert
