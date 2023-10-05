import requests
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
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

    def get_border_color(self, locator):
        border_color = self.element_is_visible(locator).value_of_css_property('border-color')
        return border_color

    def send_keys_in_field(self, locator, key):
        self.element_is_visible(locator).send_keys(key)

    def click_button(self, locator):
        self.element_is_clickable(locator).click()

    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
           This method expects to verify that the elements are present in the DOM tree,
           but not necessarily visible and displayed on the page.
           Locator - is used to find the elements.
           Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
           """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_move_to_element(self, element):
        """
        This method moves the mouse cursor to the center of the selected element, simulating a hover action.
        It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def find_element(self, locator):
        """Find element (unpacking)"""
        return self.driver.find_element(*locator)

    def fill_in_field(self, locator, key):
        """This method fills in a specified field with provided value"""
        input_field = self.element_is_visible(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(key)
        return input_field

    def get_text(self, locator):
        return self.element_is_visible(locator, 20).text

    def get_text_split(self, locator):
        return self.element_is_present(locator, 10).text.split(':')[1]

    def action_move_to_element_double_click(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).double_click().perform()

    def action_move_to_element_right_click(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).context_click().perform()

    def action_move_to_element_click(self, locator):
        """
        This method moves the mouse cursor to the center of the selected element.
        Perform a click action without navigating to a new page
        """
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def check_element_hover_style_using_js(self, element, css_property):
        """
        This method finds a visible element using the provided locator,
        simulates a hover action by moving the cursor to it,
        and then returns the value of the specified CSS property of the element using JavaScript.
        Locator - is used to find the element.
        Css_property - the name of the CSS property whose value is to be returned.
        """
        element_property = self.driver.execute_script(
            f"return getComputedStyle(arguments[0]).getPropertyValue('{css_property}');", element)
        return element_property

    def get_href(self, locator):
        href = self.element_is_visible(locator).get_attribute('href')
        return href

    def refresh_page(self):
        self.driver.refresh()

    def get_status_code(self, link):
        response = requests.get(link)
        status_code = str(response.status_code)
        return status_code

    def get_id(self, locator):
        property_id = self.element_is_visible(locator).get_property("id")
        return property_id

    def get_text_color(self, locator):
        text_color = self.find_element(locator).value_of_css_property('color')
        return text_color

    def element_is_not_visible(self, locator):
        try:
            self.element_is_visible(locator)
        except TimeoutException:
            return "Timeout"
        return True

    def switch_to_the_first_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_the_second_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
