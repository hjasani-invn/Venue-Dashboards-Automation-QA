"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        download_path = os.path.join(os.getcwd(), "Downloaded_Files")
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        #baseURL = "http://northstar-stage.us-east-1.elasticbeanstalk.com"
        baseURL = "http://admin-test.venuepositioning.com"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            # driver = webdriver.Firefox()
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        elif self.browser == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            # op = webdriver.ChromeOptions()
            # p = {'download.default_directory': 'C:\\Users\\hjasani\\Downloads'}
            # op.add_experimental_option('prefs', p)

            # Set chrome driver
            # driver = webdriver.Chrome(
            #     #"C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_106\\chromedriver.exe", options=op)
            #     #"C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_107\\chromedriver.exe")
            #     "C:\\Users\\hjasani\\OneDrive - tdkgroup\\Desktop\\work\\work\\Admin_Dashboard\\drivers\\chrome_32_109\\chromedriver.exe")
            # driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
