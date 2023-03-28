from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    #_email_filed = "//input[@id='mat-input-0']"
    _email_filed = "//input[@data-placeholder='Username']"
    # _password_filed = "//input[@id='mat-input-1']"
    _password_filed = "//input[@data-placeholder='Password']"
    _click_sign_in_btn = "//span[@class='mat-button-wrapper']"

    _click_sign_out_btn = "//div[@class='header-user-menu-label']"
    _click_log_out = "//button[@role='menuitem']"

    def enter_email(self, email):
        self.backspace_clear(self._email_filed, locatorType="xpath")
        self.sendKeys(email, self._email_filed, locatorType="xpath")

    def enter_password(self, password):
        self.backspace_clear(self._password_filed, locatorType="xpath")
        self.sendKeys(password, self._password_filed, locatorType="xpath")

    def click_login_button(self):
        self.elementClick(self._click_sign_in_btn, locatorType="xpath")
        self.hold_wait()

    def click_sign_out(self):
        self.hold_wait()
        self.elementClick(self._click_sign_out_btn, locatorType="xpath")
        self.elementClick(self._click_log_out, locatorType="xpath")
        self.hold_wait()

    def clear_fields(self):
        email_field = self.getElement(locator=self._email_filed)
        email_field.clear()

        password_filed = self.getElement(locator=self._password_filed)
        password_filed.clear()

    def login(self, email, password):
        # self.clear_fields()
        self.enter_email(email)
        self.enter_password(password)

        self.click_login_button()
        self.hold_wait()
        self.hold_wait()

    def verify_login(self):
        result = self.isElementPresent("//mat-error[@role='alert']", locatorType="xpath")
        return result
        # "//div[contains(text(), ' Wrong username or password. Please try again. ')]"

    def verify_signin(self):
        username_logo_present = self.isElementPresent(self._click_sign_out_btn, locatorType="xpath")
        return username_logo_present

    # _snackbar_xpath = "//span[contains(text(),'Authentication Failed')]"
    _snackbar_xpath = "//mat-error[contains(text(),'Wrong username or password. Please try again.')]"
    def verify_login_failed(self):
        snackbar_element = self.getElement(self._snackbar_xpath, locatorType="xpath")
        snackbar_text = snackbar_element.text
        print(snackbar_text)
        return snackbar_text