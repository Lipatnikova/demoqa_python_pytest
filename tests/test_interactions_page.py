import pytest

from data.data_urls import SORTABLE_URL
from pages.interactions_page import SortablePage


class TestSortablePage:
    def test_verify_sortable_page(self, driver):
        sortable_page = SortablePage(driver, SORTABLE_URL)
        sortable_page.open()
