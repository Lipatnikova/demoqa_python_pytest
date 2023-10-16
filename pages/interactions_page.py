import random
import time

from locators.interactions_page_locators import SortablePageLocators as Sortable
from locators.interactions_page_locators import SelectablePageLocators as Selectable
from locators.interactions_page_locators import ResizablePageLocators as Resizable
from locators.interactions_page_locators import DroppablePageLocators as Droppable
from locators.interactions_page_locators import DragabblePageLocators as Dragabble
from pages.base_page import BasePage


class SortablePage(BasePage):

    def get_all_items(self, elem):
        item_list = self.elements_are_visible(elem)
        return [item.text for item in item_list]

    def change_items(self, item):
        value = self.element_is_visible(Sortable.ALL_LOCATORS[item][0]).get_attribute('aria-selected')
        if value == 'false':
            self.click_button(Sortable.ALL_LOCATORS[item][0])
        text_before = self.get_all_items(Sortable.ALL_LOCATORS[item][1])
        item_what, item_where = random.sample(self.elements_are_visible(Sortable.ALL_LOCATORS[item][1]), k=2)
        self.action_drag_and_drop_to_element(item_what, item_where)
        text_after = self.get_all_items(Sortable.ALL_LOCATORS[item][1])
        return text_before, text_after


class SelectablePage(BasePage):

    def click_random_items(self, elem):
        item_list = self.elements_are_visible(elem)
        random.sample(item_list, k=random.randint(1, 3))
        for i in range(random.randint(1, 3)):
            item_list[i].click()

    def get_active_items(self, item):
        value = self.element_is_visible(Selectable.ALL_LOCATORS[item][0]).get_attribute("aria-selected")
        if value == 'false':
            self.click_button(Selectable.ALL_LOCATORS[item][0])
        self.click_random_items(Selectable.ALL_LOCATORS[item][1])
        active_items = self.elements_are_visible(Selectable.ALL_LOCATORS[item][2])
        return active_items


class ResizablePage(BasePage):

    def get_width_and_height(self, elem):
        width = int(elem.split(';')[0].split()[1].replace('px', ''))
        height = int(elem.split(';')[1].split()[1].replace('px', ''))
        return [width, height]

    def change_size_resizable_box(self):
        elem = self.get_attribute_style(Resizable.RESIZABLE_BOX)
        size_before = self.get_width_and_height(elem)
        handle = self.element_is_visible(Resizable.RESIZABLE_BOX_HANDLE)
        self.action_drag_and_drop_by_offset(handle, random.randint(0, 350), random.randint(0, 150))
        elem = self.get_attribute_style(Resizable.RESIZABLE_BOX)
        size_after = self.get_width_and_height(elem)
        return size_before, size_after

    def change_size_resizable(self):
        handle = self.element_is_visible(Resizable.RESIZABLE_HANDLE)
        self.go_to_element(handle)
        elem = self.get_attribute_style(Resizable.RESIZABLE)
        size_before = self.get_width_and_height(elem)
        self.action_drag_and_drop_by_offset(handle, random.randint(150, 300), random.randint(150, 300))
        time.sleep(5)
        elem = self.get_attribute_style(Resizable.RESIZABLE)
        size_after = self.get_width_and_height(elem)
        return size_before, size_after


class DroppablePage(BasePage):

    def simple_droppable(self):
        self.click_button(Droppable.SIMPLE_TAB)
        what = self.element_is_visible(Droppable.DRAG_ME_SIMPLE)
        text_before = self.get_text(Droppable.DROP_HERE_SIMPLE)
        where = self.element_is_visible(Droppable.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(what, where)
        text_after = self.get_text(Droppable.DROP_HERE_SIMPLE)
        return text_before, text_after

    def accept_droppable(self, item):
        self.click_button(Droppable.ACCEPT_TAB)
        what = self.element_is_visible(Droppable.ACCEPT_AND_NOT_ACCEPT[item])
        where = self.element_is_visible(Droppable.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(what, where)
        text = self.get_text(Droppable.DROP_HERE_ACCEPT)
        return text


class PreventPropogationPage(BasePage):

    def move_element_inside_field(self):
        self.click_button(Droppable.PREVENT_TAB)
        what = self.element_is_visible(Droppable.DRAG_ME_PREVENT)
        where = self.element_is_visible(Droppable.NOT_GREEDY_DROP_BOX)
        self.action_drag_and_drop_to_element(what, where)
        text_after_outer = self.get_text(Droppable.NOT_GREEDY_INNER_BOX_TEXT)
        text_after_inner = self.get_text(Droppable.NOT_GREEDY_DROP_BOX)
        return text_after_outer, text_after_inner

    def move_element_inside_field_greedy(self):
        self.click_button(Droppable.PREVENT_TAB)
        what = self.element_is_visible(Droppable.DRAG_ME_PREVENT)
        where = self.element_is_visible(Droppable.GREEDY_DROP_BOX)
        self.action_drag_and_drop_to_element(what, where)
        text_after_outer = self.get_text(Droppable.GREEDY_INNER_BOX_TEXT)
        text_after_inner = self.get_text(Droppable.GREEDY_DROP_BOX)
        return text_after_outer, text_after_inner


class ReverTablePage(BasePage):
    def drop_will_revertable(self):
        self.click_button(Droppable.REVERT_TAB)
        drag_div = self.element_is_visible(Droppable.WILL_REVERT)
        drop_div = self.element_is_visible(Droppable.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        return position_before, position_after

    def drop_not_revertable(self):
        self.click_button(Droppable.REVERT_TAB)
        drag_div = self.element_is_visible(Droppable.NOT_REVERT)
        drop_div = self.element_is_visible(Droppable.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        position_before = drag_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_div.get_attribute('style')
        print(position_before)
        print(position_after)
        return position_before, position_after


class DragabblePage(BasePage):

    def simple_drag(self):
        self.click_button(Dragabble.SIMPLE_TAB)
        what = self.element_is_visible(Dragabble.SIMPLE_DRAG)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, random.randint(-100, 300), random.randint(-100, 300))
        position_after = what.get_attribute("style")
        return position_before, position_after

    def get_only_x_position(self):
        self.click_button(Dragabble.AXIS_TAB)
        what = self.element_is_visible(Dragabble.ONLY_X)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, random.randint(-200, 500), 0)
        position_after = what.get_attribute("style")
        return position_before, position_after

    def get_only_y_position(self):
        self.click_button(Dragabble.AXIS_TAB)
        what = self.element_is_visible(Dragabble.ONLY_Y)
        position_before = what.get_attribute("style")
        self.action_drag_and_drop_by_offset(what, 0, random.randint(-200, 500))
        position_after = what.get_attribute("style")
        return position_before, position_after
