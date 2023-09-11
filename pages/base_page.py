from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_actual_title_of_current_page(self):
        actual_title = self.driver.title
        return actual_title

    def get_actual_url_of_current_page(self):
        actual_url = self.driver.current_url
        return actual_url

    def get_placeholder(self, locator):
        placeholder = self.element_is_visible(locator).get_attribute('placeholder')
        return placeholder

    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # def elements_are_visible(self, locator, timeout=10):
    #     """
    #     This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
    #     Visibility means that the elements are not only displayed but also have a height and width greater than 0.
    #     Locator - is used to find the elements.
    #     Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
    #     """
    #     return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    #
    def element_is_present(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # def elements_are_present(self, locator, timeout=5):
    #     """
    #        This method expects to verify that the elements are present in the DOM tree,
    #        but not necessarily visible and displayed on the page.
    #        Locator - is used to find the elements.
    #        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
    #        """
    #     return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    #
    # def element_is_clickable(self, locator, timeout=5):
    #     """
    #     This method expects to verify that the element is visible, displayed on the page, and enabled.
    #     The element is present in the DOM tree.
    #     Locator - is used to find the element.
    #     Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
    #     """
    #     return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #
    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # def action_move_to_element(self, element):
    #     """
    #     This method moves the mouse cursor to the center of the selected element, simulating a hover action.
    #     It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
    #     """
    #     action = ActionChains(self.driver)
    #     action.move_to_element(element)
    #     action.perform()
    #
    # def find_element(self, locator):
    #     """Find element (unpacking)"""
    #     return self.driver.find_element(*locator)
    #
    # def action_move_to_element_click_no_new_window(self, locator):
    #     """
    #     This method moves the mouse cursor to the center of the selected element.
    #     Perform a click action without navigating to a new page
    #     """
    #     element = self.find_element(locator)
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).click().perform()
    #
    # def fill_in_field(self, locator, value):
    #     """This method fills in a specified field with provided value"""
    #     input_field = self.element_is_clickable(locator)
    #     input_field.click()
    #     input_field.clear()
    #     input_field.send_keys(value)
    #     return input_field
    #
    # def get_text(self, locator):
    #     text = self.element_is_visible(locator, 20)
    #     return text.text
    #
    # def click_button(self, locator):
    #     btn = self.element_is_clickable(locator)
    #     btn.click()
