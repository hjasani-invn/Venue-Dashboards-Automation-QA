import os

import pytest
from base.webdriver_factory import WebDriverFactory


# @pytest.fixture()
# def setUp():
#     print("\nRunning method level setUp")
#     yield
#     print("\nRunning method level tearDown")

@pytest.fixture(scope='session')
# @pytest.fixture()
def setUp():

    print("\nRunning method level setUp")
    

    "Delete ScreenShots"
    # create folder if not available
    folder_ss = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(os.path.join(os.getcwd(), "screenshots")):
        os.mkdir(os.path.join(os.getcwd(), "screenshots"))
        print(f"screenshots folder created successfully.")
    else:
        print(f"screenshots folder already exists.")
    # downloaded_dir = os.path.join(os.getcwd(), "screenshots")
    print(folder_ss)
    for f in os.listdir(folder_ss):
        print(f)
        file_name = os.path.join(folder_ss, f)
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
            print(f"{f} is deleted successfully.")
        except:
            print(f"File {f} not found")

    "Delete Downloaded Files"
    folder_downloaded_dir = os.path.join(os.getcwd(), "Downloaded_Files")
    if not os.path.exists(os.path.join(os.getcwd(), "Downloaded_Files")):
        os.mkdir(os.path.join(os.getcwd(), "Downloaded_Files"))
        print(f"Downloaded_Files folder created successfully.")
    else:
        print(f"Downloaded_Files folder already exists.")
    # downloaded_dir = os.path.join(os.getcwd(), "Downloaded_Files")
    print(folder_downloaded_dir)
    for f in os.listdir(folder_downloaded_dir):
        print(f)
        file_name = os.path.join(folder_downloaded_dir, f)
        try:
            if os.path.exists(file_name):
                os.remove(file_name)
            print(f"{f} is deleted successfully.")
        except:
            print(f"File {f} not found")

    yield
    print("\nRunning method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\nRunning one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'chrome':
    #     baseURL = "http://northstar-stage.us-east-1.elasticbeanstalk.com"
    #     # driver = webdriver.Chrome(ChromeDriverManager().install())
    #     driver = webdriver.Chrome("C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_106\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get(baseURL)
    #     print("Running tests on Chrome")
    # else:
    #     baseURL = "http://northstar-stage.us-east-1.elasticbeanstalk.com"
    #     driver = webdriver.Firefox(executable_path="C:\\Users\\hjasani\\PycharmProjects\\Personal_Projects\\Python_Selenium\\SeleniumSessions\\chromedriver_win32_106\\chromedriver.exe")
    #     driver.get(baseURL)
    #     print("Running tests on Firefox")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nRunning one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
