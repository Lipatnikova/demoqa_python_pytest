from pages.forms_page import FormsPage
from data.data_urls import PRACTICE_FORM_URL


class TestFormsPage:
    def test_verify_fill_form_field(self, driver):
        form_page = FormsPage(driver, PRACTICE_FORM_URL)
        form_page.open()
        first_name = form_page.fill_first_name()
        last_name = form_page.fill_last_name()
        email = form_page.fill_email()
        gender = form_page.choose_gender()
        mobile = form_page.fill_mobile_number()
        day, month, year = form_page.choose_date_of_birth()
        form_page.fill_subjects()
        hobby = form_page.choose_hobbies()
        file_name = form_page.select_picture()
        address, state, city = form_page.fill_current_address_and_select_state_and_city()
        form_page.click_submit()
        input_data = [[first_name, last_name], [email], [gender], [mobile], [day.zfill(2), month, year],
                      [hobby], [file_name], [address], [state, city]]
        output_data = form_page.form_result()
        print(input_data)
        print(output_data)
        assert input_data == output_data, "Incorrect form filling or test error"
