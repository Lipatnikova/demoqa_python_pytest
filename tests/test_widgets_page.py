import time

import pytest
from data.data import AccordianData, TabData
from data.data_urls import ACCORDIAN_URL, AUTO_COMPLETE_URL, DATE_PICKER_URL, SLIDER_URL, PROGRESS_BAR_URL, TABS_URL, \
    TOOL_TIPS_URL, MENU_URL
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage
from locators.widgets_page_locators import ToolTipsPageLocators as ToolTips
from selenium.common.exceptions import TimeoutException


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

    class TestDatePickerPage:

        def test_verify_select_date(self, driver):
            date_page = DatePickerPage(driver, DATE_PICKER_URL)
            date_page.open()
            input_date, date_after = date_page.get_select_date()
            assert input_date == date_after, "Date has not changed"

        def test_verify_date_and_time(self, driver):
            date_page = DatePickerPage(driver, DATE_PICKER_URL)
            date_page.open()
            date_changes = date_page.get_date_and_time()
            date_after = date_page.get_date_after_changes()
            assert date_after == date_changes, "Date has not changed"

    class TestSliderPage:

        def test_verify_slider_change_value(self, driver):
            slider_page = SliderPage(driver, SLIDER_URL)
            slider_page.open()
            value_before = slider_page.get_slider_value()
            slider_page.change_value_slider()
            value_after = slider_page.get_slider_value()
            assert value_before != value_after, "The value in the Slider has not changed"

        def test_verify_slider_and_input_values_before_changes(self, driver):
            slider_page = SliderPage(driver, SLIDER_URL)
            slider_page.open()
            value_slider_before = slider_page.get_slider_value()
            value_input_before = slider_page.get_input_value()
            assert value_slider_before == value_input_before, \
                "The value in the slider and the input do not match"

        def test_verify_slider_and_input_values_after_changes(self, driver):
            slider_page = SliderPage(driver, SLIDER_URL)
            slider_page.open()
            slider_page.change_value_slider()
            value_slider_after = slider_page.get_slider_value()
            value_input_after = slider_page.get_input_value()
            assert value_slider_after == value_input_after, \
                "The value in the slider and the input do not match"

    class TestProgressBarPage:

        def test_verify_progress_bar_after_click_btn(self, driver):
            progress_bar_page = ProgressBarPage(driver, PROGRESS_BAR_URL)
            progress_bar_page.open()
            value_before = progress_bar_page.get_attribute_aria_valuenow_in_progress_bar()
            progress_bar_page.click_btn_start()
            progress_bar_page.random_time_sleep()
            try:
                progress_bar_page.click_btn_start()
            except TimeoutException:
                pass
            value_after = progress_bar_page.get_attribute_aria_valuenow_in_progress_bar()
            assert value_after != value_before, \
                "The value in the Progress Bar does not change"

        def test_verify_button_text_before_click_and_after_click(self, driver):
            progress_bar_page = ProgressBarPage(driver, PROGRESS_BAR_URL)
            progress_bar_page.open()
            btn_text_before = progress_bar_page.get_text_btn()
            progress_bar_page.click_btn_start()
            progress_bar_page.random_time_sleep()
            progress_bar_page.click_btn_start()
            valuenow = progress_bar_page.get_attribute_aria_valuenow_in_progress_bar()
            if valuenow < 100:
                progress_bar_page.click_btn_start()
                btn_text_after = progress_bar_page.get_text_btn()
                assert btn_text_before == 'Start' and btn_text_after == 'Stop', \
                    "The button Start/Stop/Reset contains incorrect text"
            if valuenow == 100:
                btn_text_after = progress_bar_page.get_text_btn()
                assert btn_text_before != btn_text_after and btn_text_after == 'Reset', \
                    "The button Start/Stop/Reset contains incorrect text"

    class TestTabsPage:

        @pytest.mark.parametrize('tab, text_tab', TabData.TABS)
        def test_verify_text_in_tabs_after_click_is_visible(self, driver, tab, text_tab):
            tabs_page = TabsPage(driver, TABS_URL)
            tabs_page.open()
            tabs_page.click_tab(tab)
            text = tabs_page.get_text_in_tabs(text_tab)
            assert len(text) != 0, "Text in the Tab is not displayed or is incorrect"

    class TestToolTips:
        @pytest.mark.parametrize("item", ToolTips.ALL_LOCATORS)
        def test_verify_tool_tips(self, driver, item):
            tool_tips_page = ToolTipsPage(driver, TOOL_TIPS_URL)
            tool_tips_page.open()
            tool_tips_page.hover_element(item)
            text = tool_tips_page.get_text_after_hover_tool_tips()
            assert "You hovered over the" in text, "After hover by element is not visible Tool Tips message or " \
                                                   "message does not contain expected text"

    class TestMenuPage:
        def test_verify_menu_items(self, driver):
            menu_page = MenuPage(driver, MENU_URL)
            menu_page.open()
            menu = menu_page.get_menu()
            assert menu == 8, "Menu titles are incorrect"
