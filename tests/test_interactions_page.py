import pytest

from data.data import InteractionsData
from data.data_urls import SORTABLE_URL, SELECTABLE_URL, RESIZABLE_URL, DROPPABLE_URL, DRAGABBLE_URL
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, \
    PreventPropogationPage, ReverTablePage, DragabblePage


class TestInteractionsPage:
    class TestSortablePage:

        @pytest.mark.parametrize("item", InteractionsData.LST)
        def test_sortable_page(self, driver, item):
            sortable_page = SortablePage(driver, SORTABLE_URL)
            sortable_page.open()
            before, after = sortable_page.change_items(item)
            assert before != after, "Elements have not changed"

    class TestSelectablePage:
        @pytest.mark.parametrize("item", InteractionsData.LST)
        def test_selectable_page(self, driver, item):
            selectable_page = SelectablePage(driver, SELECTABLE_URL)
            selectable_page.open()
            content = selectable_page.get_active_items(item)
            assert len(content) > 0, "Elements has not selected"

    class TestResizablePage:
        def test_resizable_box_page(self, driver):
            resizable_page = ResizablePage(driver, RESIZABLE_URL)
            resizable_page.open()
            before, after = resizable_page.change_size_resizable_box()
            assert before != after, "Window size has not changed"

        @pytest.skip
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, RESIZABLE_URL)
            resizable_page.open()
            before, after = resizable_page.change_size_resizable()
            assert before != after, "Window size has not changed"

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            simple_droppable = DroppablePage(driver, DROPPABLE_URL)
            simple_droppable.open()
            before, after = simple_droppable.simple_droppable()
            assert before != after, "The element has not been moved or the text has not changed"

        @pytest.mark.parametrize("item", InteractionsData.ACCEPT_LST)
        def test_accept_droppable(self, driver, item):
            accept_droppable = DroppablePage(driver, DROPPABLE_URL)
            accept_droppable.open()
            text = accept_droppable.accept_droppable(item[0])
            assert item[1] == text, "Wrong text after moving element"

    class TestPreventPropogationPage:
        def test_prevent_page_not_greedy(self, driver):
            prevent_page = PreventPropogationPage(driver, DROPPABLE_URL)
            prevent_page.open()
            text_after_outer, text_after_inner = prevent_page.move_element_inside_field()
            assert text_after_outer == text_after_inner, "Results should be the same"

        def test_prevent_page_greedy(self, driver):
            prevent_page = PreventPropogationPage(driver, DROPPABLE_URL)
            prevent_page.open()
            text_after_outer, text_after_inner = prevent_page.move_element_inside_field_greedy()
            assert text_after_outer != text_after_inner, "Results shouldn't be the same"

    class TestReverTablePage:

        def test_verify_revert_droppable(self, driver):
            revert_droppable_page = ReverTablePage(driver, DROPPABLE_URL)
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_will_revertable()
            assert before != after, "Incorrect element movement"

        def test_verify_not_revert_droppable(self, driver):
            revert_droppable_page = ReverTablePage(driver, DROPPABLE_URL)
            revert_droppable_page.open()
            before, after = revert_droppable_page.drop_not_revertable()
            assert before == after, "Incorrect element movement"

    class TestDragabblePage:
        def test_verify_simple_dragable_page(self, driver):
            drag_able_page = DragabblePage(driver, DRAGABBLE_URL)
            drag_able_page.open()
            before, after = drag_able_page.simple_drag()
            assert before != after, "Element has not been moved"

        def test_verify_simple_dragable_page_only_x(self, driver):
            drag_able_page = DragabblePage(driver, DRAGABBLE_URL)
            drag_able_page.open()
            before, after = drag_able_page.get_only_x_position()
            assert before != after, "Element has not been moved"
