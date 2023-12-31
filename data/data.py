import pytest
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
    BTN_IN_ALERT = ["accept", "dismiss"]


class FramesData:
    SIZE_FRAME = ["small", "big"]


class ModalData:
    CLOSE_MODAL = ["Esc", "button", "cross", "Tab and Enter"]


class AccordianData:
    TITLE_TEXT = ["what", "where", "why"]


class TabData:
    TABS = [((By.CSS_SELECTOR, "a[id='demo-tab-what']"), (By.CSS_SELECTOR, "#demo-tabpane-what > p")),
            ((By.CSS_SELECTOR, "a[id='demo-tab-origin']"), (By.CSS_SELECTOR, "#demo-tabpane-origin > p.mt-3")),
            ((By.CSS_SELECTOR, "a[id='demo-tab-use']"), (By.CSS_SELECTOR, "#demo-tabpane-use > p.mt-3")),
            (pytest.param((By.CSS_SELECTOR, "a[id='demo-tab-more']"),
                          (By.CSS_SELECTOR, "#demo-tabpane-more > p.mt-3"), marks=pytest.mark.xfail))]


class InteractionsData:
    LST = ["list", "grid"]
    ACCEPT_LST = [("acceptable", "Dropped!"), ("not_acceptable", "Drop here")]


class FormsData:
    SUBJECT = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
               "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]

