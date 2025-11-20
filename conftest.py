import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ

@pytest.fixture(scope='function')
def driver(request):
    project_name = environ.get('BROWSERSTACK_PROJECT_NAME')
    build = environ.get('BROWSERSTACK_BUILD_NAME')
    username = environ.get('BROWSERSTACK_USERNAME')
    access_key = environ.get('BROWSERSTACK_ACCESS_KEY')

    selenium_endpoint = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

    chrome_options = Options()

    # Browser capabilities
    chrome_options.set_capability("browserName", "Chrome")
    chrome_options.set_capability("browserVersion", "latest")

    # BrowserStack capabilities
    bstack_options = {
        "os": "Windows",
        "osVersion": "10",
        "userName": username,
        "accessKey": access_key,
        "projectName": project_name,
        "buildName": build,
        "sessionName": request.node.name,
        "local": False,
    }

    chrome_options.set_capability("bstack:options", bstack_options)

    # Add Chrome args (correct location!)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=chrome_options
    )

    yield driver

    driver.quit()