import random
import time
from generator.generator import generator_color, generator_date, random_num_up_to_one_hundred, random_num
from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators as Accordian
from locators.widgets_page_locators import AutoCompletePageLocators as AutoComplete
from locators.widgets_page_locators import DatePickerPageLocators as DatePicker
from locators.widgets_page_locators import SliderPageLocators as Slider
from locators.widgets_page_locators import ProgressBarPageLocators as ProgressBar
from locators.widgets_page_locators import ToolTipsPageLocators as ToolTip
from locators.widgets_page_locators import MenuPageLocators as Menu
from locators.widgets_page_locators import SelectMenuPageLocators as SelectLoc
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


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


class DatePickerPage(BasePage):

    def get_month_number_by_name(self, item):
        months_dict = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        return months_dict[item]

    def get_select_date(self):
        info = next(generator_date())
        year = info.year
        month = info.month
        day = info.day
        input_date = self.element_is_visible(DatePicker.SELECT_DATE)
        input_date.click()
        self.set_date_by_value(DatePicker.SELECT_DATE_YEAR, year)
        self.set_date_by_value(DatePicker.SELECT_DATE_MONTH, month)
        self.set_date_from_list(DatePicker.SELECT_DATE_DAYS, day)
        selected_date = f"{str(self.get_month_number_by_name(month)).zfill(2)}/{day}/{year}"
        date_after = input_date.get_attribute('value')
        return selected_date, date_after

    def set_date_by_value(self, item, value):
        select = Select(self.element_is_clickable(item))
        select.select_by_visible_text(value)

    def set_date_from_list(self, item, value):
        select = self.elements_are_present(item)
        for i in select:
            if i.text == value:
                time.sleep(1)
                i.click()
                break

    def set_date_with_go_to_element(self, item, value):
        select = self.elements_are_present(item)
        for i in select:
            if i.text == value:
                self.go_to_element(i)
                time.sleep(1)
                i.click()
                break

    def get_year(self):
        self.click_button(DatePicker.DATE_AND_TIME_YEAR)
        time.sleep(1)
        lst = random.choice(self.elements_are_present(DatePicker.DATE_AND_TIME_YEAR_LIST)[1:-1])
        self.go_to_element(lst)
        year = lst.text
        lst.click()
        return year

    def get_month(self):
        self.click_button(DatePicker.DATE_AND_TIME_MONTH)
        time.sleep(1)
        lst = random.choice(self.elements_are_present(DatePicker.DATE_AND_TIME_MONTH_LIST))
        self.go_to_element(lst)
        month = lst.text
        lst.click()
        return month

    def get_time(self):
        info = next(generator_date())
        time_info = info.time
        self.set_date_with_go_to_element(DatePicker.DATE_AND_TIME_TIME_LIST, time_info)
        return time_info

    def convert_to_12h_format(self, time_24h):
        time_24h_parts = time_24h.split(':')
        hour = int(time_24h_parts[0])
        minute = time_24h_parts[1]
        am_pm = 'AM'
        if hour == 0:
            hour = 12
        elif hour >= 12:
            am_pm = 'PM'
            if hour > 12:
                hour -= 12
        return f"{hour}:{minute} {am_pm}"

    def get_date_and_time(self):
        info = next(generator_date())
        day = info.day
        input_date = self.element_is_visible(DatePicker.DATE_AND_TIME_INPUT)
        input_date.click()
        year = self.get_year()
        month = self.get_month()
        self.set_date_from_list(DatePicker.SELECT_DATE_DAYS, day)
        time_date = self.get_time()
        time.sleep(1)
        input_date = f"{month} {day}, {year} {self.convert_to_12h_format(time_date)}"
        return input_date

    def get_date_after_changes(self):
        self.go_to_element(self.element_is_present(DatePicker.DATE_AND_TIME_INPUT))
        time.sleep(1)
        date_after = self.element_is_present(DatePicker.DATE_AND_TIME_INPUT).get_attribute('value')
        return date_after


class SliderPage(BasePage):

    def get_slider_value(self):
        return self.get_attribute_value(Slider.SLIDER_INPUT)

    def change_value_slider(self):
        slider = self.element_is_visible(Slider.SLIDER_INPUT)
        x = random_num_up_to_one_hundred()
        self.action_drag_and_drop_by_offset(slider, x, 0)
        return x

    def get_input_value(self):
        return self.get_attribute_value(Slider.SLIDER_INPUT)


class ProgressBarPage(BasePage):

    def click_btn_start(self):
        self.click_button(ProgressBar.BUTTON_START_STOP)

    def get_text_btn(self):
        text_btn = self.get_text(ProgressBar.BUTTON_START_STOP)
        return text_btn

    def click_btn_reset(self):
        self.click_button(ProgressBar.BUTTON_RESET)

    def get_attribute_aria_valuenow_in_progress_bar(self):
        return int(self.get_attribute_aria_valuenow(ProgressBar.VALUE_PROGRESS_BAR))

    def random_time_sleep(self):
        time.sleep(random_num())


class TabsPage(BasePage):

    def click_tab(self, locator):
        try:
            self.click_button(locator)
        except ElementClickInterceptedException:
            print('\n', 'Tab with locator:', locator, 'is not clickable')

    def get_text_in_tabs(self, locator):
        return self.get_text(locator)


class ToolTipsPage(BasePage):

    def hover_element(self, locator):
        elem = self.element_is_visible(locator, 15)
        self.action_move_to_element(elem)

    def get_text_after_hover_tool_tips(self):
        return self.get_text(ToolTip.AFTER_HOVER_TEXT)


class MenuPage(BasePage):
    def get_menu(self):
        menu_list = self.elements_are_present(Menu.MENU_LIST)
        return len(menu_list)


class SelectMenuPage(BasePage):
    def click_select_value(self):
        self.click_button(SelectLoc.SELECT_VALUE)

    def get_select_value_and_click(self):
        text = self.elements_are_present(SelectLoc.SELECT_VALUE_ITEMS)
        item = random.choice(text)
        input_text = item.text
        item.click()
        return input_text

    def get_text_select_value(self):
        check_text = self.get_text(SelectLoc.SELECT_VALUE_CHECK)
        return check_text

    def click_select_one(self):
        self.click_button(SelectLoc.SELECT_ONE)

    def get_select_one_and_click(self):
        text = self.elements_are_present(SelectLoc.SELECT_VALUE_ITEMS)
        item = random.choice(text)
        input_text = item.text
        item.click()
        return input_text

    def get_text_select_one(self):
        check_text = self.get_text(SelectLoc.SELECT_VALUE_CHECK)
        return check_text

    def get_selected_option_in_select_old_style(self):
        select_elem = self.element_is_visible(SelectLoc.SELECT_OLD_STYLE)
        # Создаем объект класса Select
        select_list = Select(select_elem)
        # Получаем список всех элементов списка
        options = select_list.options
        # Выбираем случайный элемент из списка
        random_option = random.choice(options)
        # Сохраняем текст выбранного элемента в переменную
        selected_option_text = random_option.text
        # Кликаем на выбранный элемент
        random_option.click()
        time.sleep(2)
        # Находим выбранный элемент по тексту
        selected_option = select_list.first_selected_option
        return selected_option.text, selected_option_text

    def get_selected_option_in_select_multi(self):
        select_elem = self.element_is_visible(SelectLoc.SELECT_MULTI)
        select_list = Select(select_elem)
        options = select_list.options
        random_option = random.choice(options)
        selected_option_text = random_option.text
        random_option.click()
        time.sleep(2)
        selected_option = select_list.first_selected_option
        return selected_option.text, selected_option_text
