from generator.generator import get_person
from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators as LocWin
from locators.alerts_frame_windows_page_locators import AlertsPageLocators as LocAlert
from locators.alerts_frame_windows_page_locators import FramePageLocators as LocFrame
from locators.alerts_frame_windows_page_locators import NestedFramePageLocators as LocNestedFrame
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    def click_btn_new_tab(self):
        self.click_button(LocWin.NEW_TAB_BTN)

    def click_btn_new_window(self):
        self.click_button(LocWin.NEW_WINDOW_BTN)

    def click_btn_new_window_msg(self):
        self.click_button(LocWin.NEW_WINDOW_MESSAGE_BTN)

    def get_link_in_the_new_tab(self):
        self.switch_to_the_x_window(1)
        return self.get_actual_url_of_current_page()

    def get_count_windows(self):
        handles = self.driver.window_handles
        return len(handles)

    def get_heading_text_in_new_window(self):
        return self.get_text(LocWin.SAMPLE_PAGE)


class AlertsPage(BasePage):

    def click_btn_see_alert(self):
        self.click_button(LocAlert.BUTTON_ALERT)

    def click_btn_see_alert_will_appear_after_five_seconds(self):
        self.click_button(LocAlert.BUTTON_ALERT_AFTER_5_SECOND)

    def click_btn_confirm_box_will_appear(self):
        self.click_button(LocAlert.BUTTON_CONFIRM_BOX)

    def click_btn_prompt_box_will_appear(self):
        self.click_button(LocAlert.BUTTON_PROMPT)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_text_result_after_click_confirm_in_alert(self):
        return self.get_text(LocAlert.CONFIRM_BOX_TEXT)

    def complex_alert(self, item):
        alert = self.driver.switch_to.alert
        if item == "accept":
            alert.accept()
            text = "Ok"
        else:
            alert.dismiss()
            text = "Cancel"
        return text

    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        info = next(get_person())
        first_name = info.first_name
        alert.send_keys(first_name)
        alert.accept()
        return first_name

    def get_text_result_after_click_prompt_in_alert(self):
        return self.get_text(LocAlert.PROMPT_TEXT)


class FramesPage(BasePage):

    def first_frame_is_present(self):
        return self.element_is_present(LocFrame.BIG_FRAME)

    def second_frame_is_present(self):
        return self.element_is_present(LocFrame.SMALL_FRAME)

    def get_count_frames_on_the_page(self):
        return len(self.elements_are_present(LocFrame.FRAMES))

    def get_frame_info(self, item):
        if item == "small":
            frame = self.first_frame_is_present()
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.get_text(LocFrame.FRAME_PAGE)
            self.driver.switch_to.default_content()
            return [width, height, text]
        if item == "big":
            frame = self.first_frame_is_present()
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.get_text(LocFrame.FRAME_PAGE)
            self.driver.switch_to.default_content()
            return [width, height, text]


class NestedFramesPage(BasePage):

    def nested_frame_page_text_first_frame(self):
        first_frame = self.element_is_present(LocNestedFrame.FIRST_FRAME)
        self.driver.switch_to.frame(first_frame)
        text_first_frame = self.get_text(LocNestedFrame.FIRST_FRAME_TEXT)
        return text_first_frame

    def nested_frame_page_text_second_frame(self):
        second_frame = self.element_is_present(LocNestedFrame.SECOND_FRAME)
        self.driver.switch_to.frame(second_frame)
        text_second_frame = self.get_text(LocNestedFrame.SECOND_FRAME_TEXT)
        return text_second_frame
