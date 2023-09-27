from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    FIELDS = [FULL_NAME, EMAIL, CURRENT_ADDRESS, PERMANENT_ADDRESS]

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    TITLE_QUESTION = (By.CSS_SELECTOR, "div.mb-3")
    RADIO_BTN = (By.CSS_SELECTOR, "[class*='custom-radio custom-control-inline']")
    YES_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON_BTN = (By.XPATH, "//button[text()='Click Me']")

    MSG_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    MSG_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    MSG_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:

    # Following links will open new tab
    HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    HOME_DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    HOMES_LINKS = [HOME_LINK, HOME_DYNAMIC_LINK]
    TEXT_AFTER_CLICK = (By.CSS_SELECTOR, "p[id='linkResponse']")


class BrokenLinksImageLocators:
    BROKEN_IMAGE = (By.XPATH, "//img[contains(@src, 'Toolsqa_1.jpg')]")
    IMAGE = (By.XPATH, "//img[contains(@src, '/images/Toolsqa.jpg'))]")
    IMG = [IMAGE, BROKEN_IMAGE]
    VALID_LINK = (By.XPATH, '//*[contains(@href, "http://demoqa.com")]')
    BROKEN_LINK = (By.XPATH, '//a[contains(@href, "http://the-internet.herokuapp.com/status_codes/500")]')
    LINKS = [VALID_LINK, BROKEN_LINK]


class UploadAndDownloadPageLocators:
    DOWNLOAD_BTN = (By.CSS_SELECTOR, "a[id='downloadButton']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")


class DynamicPropertiesPageLocators:
    RANDOM_ID_TEXT = (By.XPATH, "//*[@id='app']/div/div/div/div/div/p[1]")
    ENABLE_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, " button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, " button[id='visibleAfter']")
