from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        log = cl.customLogger(logging.DEBUG)
        # locators
        # self._email_field = "//input[@id='inputEmail3']"
        # self._password_field = "//input[@id='inputPassword3']"
        # self._signin_button = "//button[contains(text(),'Sign in')]"
        # self._forgot_pass_button = "//button[contains(text(),'Forgot Password')]"
        # self._user_button = "//div[@class='user-profile']"
        # self._signout_button = "//a[contains(text(), 'Sign out')]"

    _email_field = "//input[@type='email']"
    _password_field = "//input[@id='inputPassword3']"
    _signin_button = "//button[contains(text(),'Sign in')]"
    _forgot_pass_button = "//button[contains(text(),'Forgot Password')]"
    _user_button = "//div[@class='user-profile']"
    _signout_button = "//a[contains(text(), 'Sign out')]"

    def enterEmail(self, email):
        self.backspace_clear(self._email_field, locatorType="xpath")
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.backspace_clear(self._password_field, locatorType="xpath")
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._signin_button, locatorType="xpath")

    def clickForgotPasswordButton(self):
        self.elementClick(self._forgot_pass_button, locatorType="xpath")

    def login(self, email, password):
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.hold_wait()
        self.hold_wait()

    def sign_out(self):
        self.hold_wait()
        self.elementClick(self._user_button, locatorType="xpath")
        self.elementClick(self._signout_button, locatorType="xpath")
        self.hold_wait()

    def clearFields(self):
        self.backspace_clear(self._email_field, locatorType="xpath")
        self.backspace_clear(self._password_field, locatorType="xpath")
        # self.getElement(locator=self._email_field).clear()
        # self.getElement(locator=self._password_field).clear()
