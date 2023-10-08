from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BTN = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BTN = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_WINDOW_MESSAGE_BTN = (By.CSS_SELECTOR, "button[id='messageWindowButton']")
    BTNS_FOR_CLICK = [NEW_TAB_BTN, NEW_WINDOW_BTN]
    SAMPLE_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    BUTTON_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    BUTTON_ALERT_AFTER_5_SECOND = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    BUTTON_CONFIRM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    BUTTON_PROMPT = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramePageLocators:
    FRAMES = (By.TAG_NAME, "iframe")
    BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMALL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    FRAME_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FIRST_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    SECOND_FRAME = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    SECOND_FRAME_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BTN = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    LARGE_MODAL_BTN = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    MODAL_HEADER = (By.CSS_SELECTOR, "div[class='modal-title h4']")
    MODAL_TITLE = (By.CSS_SELECTOR, "div[class='modal-body']")
    MODAL_CLOSE_CROSS = (By.CSS_SELECTOR, "button[class='close']")
    CLOSE_BUTTON_SMALL_MODAL = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    CLOSE_BUTTON_LARGE_MODAL = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
