import logging
import time

from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            # print("Locator type " + locatorType + " not correct/supported")
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            # print("Element Found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            # print("Element not found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            # print("Elements Found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Elements Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            # print("Elements not found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Elements not found with locator: " + locator + " and locatorType: " + locatorType)
        return elements

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            # print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            # print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def double_clicks(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.double_click(element).perform()
            self.log.info("double Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info(
                "Cannot double click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            # print("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            # print("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found---------")
                return True
            else:
                self.log.info("Element not found-------")
                return False
        except:
            self.log.info("Element not found-------")
            return False

    # def elementPresenceCheck(self, locator, byType):
    def elementPresenceCheck(self, locator, locatorType="id"):
        try:
            elementList = self.driver.find_elements(locator, locatorType="id")
            # elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element not present")
                return True
            else:
                self.log.info("Element not present")
                return False
        except:
            self.log.info("Element not present")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def hold_wait(self):
        time.sleep(2)

    # def get_text(self, locator,locatorType="id"):
    #     element = None
    #     try:
    #         locatorType = locatorType.lower()
    #         byType = self.getByType(locatorType)
    #         element = self.driver.find_element(byType, locator)
    #         txt = element.text()
    #         # print("Element Found with locator: " + locator + " and locatorType: " + locatorType)
    #         self.log.info("Element Text Found with locator: " + locator + " and locatorType: " + locatorType)
    #     except:
    #         # print("Element not found with locator: " + locator + " and locatorType: " + locatorType)
    #         self.log.info("Element Text not found with locator: " + locator + " and locatorType: " + locatorType)
    #     return element

    def is_selected(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.is_selected()
            self.log.info(
                "Check box is already selected on element with locator: " + locator + " locatorType: " + locatorType)
            return True
        except:
            self.log.info(
                "Check box is not selected on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
            return False

    def is_select(self, locator, locatorType="id"):
        self.log.info("is_select method called: ")
        return self.driver.is_selected()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()

        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.driver.execute_script('return window.innerHeight') / 2) + self.driver.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        return self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

        # return self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def backspace_clear(self, locator, locatorType="id"):
        try:
            l = self.getElement(locator, locatorType)
            l.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
            self.log.info("data clear with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("data cannot be wiped with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def click_and_drag(self, to_pos):
        action = ActionChains(self.driver)
        action.move_by_offset(to_pos[0], to_pos[1]).perform()

    # def drag_and_drop_offset(self,locator, locatorType="id"):
    #     element = self.elementClick(locator, locatorType)
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop_by_offset(element, 100, 200)
    #     action.perform()


    # def click_and_drag(self):
    #     action = ActionChains(self.driver)
    #     time.sleep(4)
    #     action.move_by_offset(300, 500).perform()
    #     time.sleep(3)

    def refresh_page(self):
        self.driver.refresh()

    def hover_over_mouse(self):
        "Action Class"
        pass

    # def drag_drop(self, locator, locatorType="xpath"):
    #     src = self.getElement(locator, locatorType)
    #     trg = self.getElement(locator, locatorType)
    #     action = ActionChains(self.driver)
    #     time.sleep(2)
    #     action.drag_and_drop(src, trg).perform()
    #     time.sleep(2)

    def drag_drop(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            # print("Element Found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Drag and Drop Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            # print("Element not found with locator: " + locator + " and locatorType: " + locatorType)
            self.log.info("Drag and Drop Element not found with locator: " + locator + " and locatorType: " + locatorType)

        action = ActionChains(self.driver)
        time.sleep(2)
        action.drag_and_drop(element, element).perform()
        time.sleep(2)
        return element

    def drag(self, locator, locatorType="xpath"):
        source1 = None
        target1 = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            source1 = self.driver.find_element(byType, locator)
            target1 = self.driver.find_element(byType, locator)
            action = ActionChains(self.driver)
            time.sleep(2)
            action.drag_and_drop(source1, target1).perform()
            time.sleep(2)
        except:
            self.log.info("Drag and Drop Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return source1, target1


