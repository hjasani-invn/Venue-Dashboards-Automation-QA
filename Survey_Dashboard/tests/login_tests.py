import pytest
from pages.login_page import LoginPage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.login
    @pytest.mark.run(1)
    def test_3_1_1_login_valid(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.loginpage.sign_out()

    @pytest.mark.login
    @pytest.mark.run(2)
    def test_3_1_2_login_bad_password(self):
        self.loginpage.login("AutomationTestUser001", "Thisisthewrongpassword")

    @pytest.mark.login
    @pytest.mark.run(3)
    def test_3_1_3_login_bad_user(self):
        self.loginpage.login("NotARealUser@invensense.com", "NotARealPassword")

    @pytest.mark.login
    @pytest.mark.run(4)
    def test_3_1_4_forgot_pwrd(self):
        # ERROR for site owner:Invalid domain for site key
        pass

