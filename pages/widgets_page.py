import random
from generator.generator import generator_color
from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators as Accordian
from locators.widgets_page_locators import AutoCompletePageLocators as AutoComplete
from selenium.webdriver import Keys


class AccordianPage(BasePage):

    def click_button_what(self):
        self.click_button(Accordian.WHAT)

    def click_button_where(self):
        self.click_button(Accordian.WHERE)

    def click_button_why(self):
        self.click_button(Accordian.WHY)

    def get_text_in_cards(self, item):
        if item == "what":
            content = self.get_text(Accordian.WHAT)
            return content, "What is Lorem Ipsum?"
        elif item == "where":
            content = self.get_text(Accordian.WHERE)
            return content, "Where does it come from?"
        elif item == "why":
            content = self.get_text(Accordian.WHY)
            return content, "Why do we use it?"

    def get_content_from_card(self, item):
        if item == "what":
            check_attribute = self.get_attribute_class(Accordian.WHAT_CONTENT_CHECK)
            if check_attribute == "collapse show":
                content = self.get_text(Accordian.WHAT_CONTENT)
                return content
            else:
                self.click_button_what()
                content = self.get_text(Accordian.WHAT_CONTENT)
                return content
        elif item == "where":
            self.click_button_what()
            self.click_button_where()
            check_attribute = self.get_attribute_class(Accordian.WHERE_CONTENT_CHECK)
            if check_attribute == "collapse show":
                content = self.get_text(Accordian.WHERE_CONTENT)
                return content
            else:
                self.click_button_where()
                content = self.get_text(Accordian.WHERE_CONTENT)
                return content
        elif item == "why":
            self.click_button_what()
            self.click_button_why()
            check_attribute = self.get_attribute_class(Accordian.WHY_CONTENT_CHECK)
            if check_attribute == "collapse show":
                content = self.get_text(Accordian.WHY_CONTENT)
                return content
            else:
                self.click_button_why()
                content = self.get_text(Accordian.WHY_CONTENT)
                return content


class AutoCompletePage(BasePage):

    def fill_input_multi(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(3, 5))
        for color in colors:
            input_multi = self.element_is_clickable(AutoComplete.MULTI_COLOR)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def check_colors_in_field(self):
        colors = self.elements_are_present(AutoComplete.MULTI_COLOR_VALUE)
        lst = []
        for color in colors:
            lst.append(color.text)
        return lst

    def click_btn_remove_all_colors(self):
        self.click_button(AutoComplete.REMOVE_ALL_COLORS)

    def remove_all_colors(self):
        output = self.get_text(AutoComplete.MULTI_COLOR)
        return output

    def remove_some_colors(self):
        all_colors = self.fill_input_multi()
        random.shuffle(all_colors)
        random_color = all_colors[0:random.randint(1, 2)]
        remove_color_name = []
        for i in self.elements_are_present(AutoComplete.GET_COLOR_NAME):
            if i.text in random_color:
                remove_color_name.append(i.text)
                self.click_button(AutoComplete.REMOVE_ONE_COLOR)
        return remove_color_name, all_colors

    def fill_single_color_field(self):
        colors = random.sample(next(generator_color()).color_name, k=1)
        for color in colors:
            input_single = self.element_is_clickable(AutoComplete.SINGLE_COLOR_INPUT)
            input_single.send_keys(color)
            input_single.send_keys(Keys.ENTER)
        return colors[0]

    def get_text_single_color_field(self):
        return self.get_text(AutoComplete.SINGLE_COLOR_NAME)

