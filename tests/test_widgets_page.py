import pytest
from data.data import AccordianData
from data.data_urls import ACCORDIAN_URL
from pages.widgets_page import AccordianPage


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
