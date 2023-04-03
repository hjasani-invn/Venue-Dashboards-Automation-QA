import time

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

    _forgot_password_page_xpath = "//h1[contains(text(),'Enter User Id / Email to continue')]"
    def verify_if_on_reset_password_page(self):
        page_text_element = self.getElement(self._forgot_password_page_xpath, locatorType="xpath")
        time.sleep(1)
        if page_text_element.text == "Enter User Id / Email to continue":
            assert True
            time.sleep(1)
        else:
            assert False

    def login(self, email, password):
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.hold_wait()
        self.hold_wait()

    def sign_out(self):
        try:
            self.waitForElement(self._user_button, locatorType="xpath")
            self.elementClick(self._user_button, locatorType="xpath")
            self.elementClick(self._signout_button, locatorType="xpath")
            self.hold_wait()
        except:
            print("User Profile is not clickable")

    def clearFields(self):
        self.backspace_clear(self._email_field, locatorType="xpath")
        self.backspace_clear(self._password_field, locatorType="xpath")
        # self.getElement(locator=self._email_field).clear()
        # self.getElement(locator=self._password_field).clear()


    _user_visible = "//div[@class='user-profile']"
    def verify_sign_in(self):
        is_visible = self.isElementPresent(self._user_visible, locatorType="xpath")
        return is_visible

    _authetication_failed_bad_password = "//div[contains(text(),'AuthenticationError Invalid UserId or Password')]"
    def verify_bad_password(self):
        is_visible = self.isElementPresent(self._authetication_failed_bad_password, locatorType="xpath")
        return is_visible

    _authetication_failed_bad_usr = "//div[contains(text(),'Authentication Failed!!')]"
    def verify_bad_user(self):
        is_visible = self.isElementPresent(self._authetication_failed_bad_usr, locatorType="xpath")
        return is_visible

    _txt_available = "//h1[contains(text(),'Enter User Id / Email to continue')]"
    def verify_forgot_password(self):
        is_navigated_to_forget_password_page = self.isElementPresent(self._txt_available, locatorType="xpath")
        return is_navigated_to_forget_password_page