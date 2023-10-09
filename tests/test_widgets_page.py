import pytest
from data.data import AccordianData
from data.data_urls import ACCORDIAN_URL, AUTO_COMPLETE_URL
from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgetsPage:

    class TestAccordian:

        @pytest.mark.parametrize('item', AccordianData.title_text)
        def test_verify_accordian_title(self, driver, item):
            accordian_page = AccordianPage(driver, ACCORDIAN_URL)
            accordian_page.open()
            text, check = accordian_page.get_text_in_cards(item)
            assert text == check, "Title is incorrect"

        @pytest.mark.parametrize('item', AccordianData.title_text)
        def test_verify_accordian_content(self, driver, item):
            accordian_page = AccordianPage(driver, ACCORDIAN_URL)
            accordian_page.open()
            text = accordian_page.get_content_from_card(item)
            assert len(text) > 100, "Content is empty"

    class TestAutoCompletePage:

        def test_verify_multi_colors(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            input_colors = auto_complete_page.fill_input_multi()
            output_color = auto_complete_page.check_colors_in_field()
            assert input_colors == output_color, "Input data does not match output"

        def test_remove_all_color(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            input_color = auto_complete_page.fill_input_multi()
            auto_complete_page.click_btn_remove_all_colors()
            output_color = auto_complete_page.remove_all_colors()
            assert len(input_color) > len(output_color) == 0, "After deleting all elements, the field is not empty"

        def test_remove_some_colors(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            deleted_colors, all_colors = auto_complete_page.remove_some_colors()
            assert set(deleted_colors).issubset(set(all_colors)) and len(deleted_colors) < len(all_colors), \
                """The removed colors aren't in the main list, or the length of the removed colors is greater than or 
                equal to the main list"""

        def test_verify_remove_all_color(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            input_color = auto_complete_page.fill_input_multi()
            output_color = auto_complete_page.remove_all_colors()
            assert len(input_color) > len(output_color) == 0, \
                "After deleting all elements, the field is not empty"

        def test_verify_remove_some_colors(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            deleted_colors, all_colors = auto_complete_page.remove_some_colors()
            assert set(deleted_colors).issubset(set(all_colors)) and len(deleted_colors) < len(all_colors), \
                """The removed colors aren't in the main list, or the length of the removed colors is greater than or 
                equal to the main list"""

        def test_verify_single_color(self, driver):
            auto_complete_page = AutoCompletePage(driver, AUTO_COMPLETE_URL)
            auto_complete_page.open()
            input_color = auto_complete_page.fill_single_color_field()
            output_color = auto_complete_page.get_text_single_color_field()
            assert input_color == output_color, "Selected color is wrong"
