from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators as Accordian


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
