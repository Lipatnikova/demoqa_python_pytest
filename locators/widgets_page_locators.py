from selenium.webdriver.common.by import By


class AccordianPageLocators:
    WHAT = (By.CSS_SELECTOR, "div[id='section1Heading']")
    WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content']")
    WHAT_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section1Heading']~div")
    WHERE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    WHERE_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content']")
    WHERE_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section2Heading']~div")
    WHY = (By.CSS_SELECTOR, "div[id='section3Heading']")
    WHY_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content']")
    WHY_CONTENT_CHECK = (By.CSS_SELECTOR, "div[id='section3Heading']~div")


class AutoCompletePageLocators:
    MULTI_COLOR = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_COLOR_VALUE = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value']")
    REMOVE_ALL_COLORS = (By.XPATH, "//div[contains(@class, 'auto-complete__clear-indicator')]")
    GET_COLOR_NAME = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value__label']")
    REMOVE_ONE_COLOR = (By.CSS_SELECTOR, "div[class$='auto-complete__multi-value__remove']")
    SINGLE_COLOR_NAME = (By.CSS_SELECTOR, "div[class^='auto-complete__single-value']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    SELECT_DATE = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_DATE_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_DATE_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_DATE_DAYS = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class^='range-slider']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")


class ProgressBarPageLocators:
    BUTTON_START_STOP = (By.CSS_SELECTOR, "button[id='startStopButton']")
    BUTTON_RESET = (By.CSS_SELECTOR, "button[id='resetButton']")
    VALUE_PROGRESS_BAR = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class ToolTipsPageLocators:
    ALL_LOCATORS = [(By.CSS_SELECTOR, "button[id='toolTipButton']"),
                    (By.CSS_SELECTOR, "input[id='toolTipTextField']"),
                    (By.XPATH, "//div[@id='texToolTopContainer']/a[contains(text(), 'Contrary')]"),
                    (By.CSS_SELECTOR, "#texToolTopContainer > a:nth-child(2)")
                    ]
    AFTER_HOVER_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")


class MenuPageLocators:
    MENU_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuPageLocators:
    SELECT_VALUE = (By.CSS_SELECTOR, "div[id='withOptGroup']")
    SELECT_VALUE_ITEMS = (By.CSS_SELECTOR, " div[tabindex='-1']")
    SELECT_VALUE_CHECK = (By.CSS_SELECTOR, " div[class$='singleValue']")
    SELECT_ONE = (By.CSS_SELECTOR, "div[id='selectOne']")
    SELECT_OLD_STYLE = (By.CSS_SELECTOR, "select[id='oldSelectMenu']")
    SELECT_MULTI = (By.CSS_SELECTOR, "select[id='cars']")
