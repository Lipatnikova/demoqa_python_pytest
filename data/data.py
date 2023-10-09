from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None
    mobile: str = None


@dataclass
class Color:
    color_name: list = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None


class LinksAndUrls:
    # Following links will send an api call
    LINKS_AND_URLS = [((By.CSS_SELECTOR, "a[id='created']"), "https://demoqa.com/created"),
                      ((By.CSS_SELECTOR, "a[id='no-content']"), "https://demoqa.com/no-content"),
                      ((By.CSS_SELECTOR, "a[id='moved']"), "https://demoqa.com/moved"),
                      ((By.CSS_SELECTOR, "a[id='bad-request']"), "https://demoqa.com/bad-request"),
                      ((By.CSS_SELECTOR, "a[id='unauthorized']"), "https://demoqa.com/unauthorized"),
                      ((By.CSS_SELECTOR, "a[id='forbidden']"), "https://demoqa.com/forbidden"),
                      ((By.CSS_SELECTOR, "a[id='invalid-url']"), "https://demoqa.com/invalid-url")
                      ]


class AlertsData:
    btn_in_alert = ["accept", "dismiss"]


class FramesData:
    size_frame = ["small", "big"]


class ModalData:
    close_modal = ["Esc", "button", "cross", "Tab and Enter"]


class AccordianData:
    title_text = ["what", "where", "why"]
