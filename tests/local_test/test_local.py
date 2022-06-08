from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

def test_local(selenium):
  # # Creates an instance of Local
  bs_local = Local()

  # # You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
  # bs_local_args = { "key": "BROWSERSTACK_ACCESS_KEY" }

  # # Starts the Local instance with the required arguments
  # bs_local.start(**bs_local_args)

  # # Check if BrowserStack local instance is running
  # print('Check Local: ', bs_local.isRunning())

  # desired_cap = {
  #   "bstack:options" : {
  #     "os" : "OS X",
  #     "osVersion" : "Monterey",
  #     "buildName" : "PyTest Example Project",
  #     "sessionName" : "OSX Monterey Chrome Latest - Local Test",
  #     "local" : "true",
  #     "seleniumVersion" : "4.1.2"
  #   },
  #   "browserName" : "Chrome",
  #   "browserVersion" : "latest"
  # }

  # driver = webdriver.Remote(
  #   command_executor='https://<BROWSERSTACK_USER_NAME>:<BROWSERSTACK_ACCESS_KEY>@hub-cloud.browserstack.com/wd/hub',
  #   desired_capabilities=desired_cap)

  # Checks if local site is running
  # selenium.maximize_window()
  selenium.get('http://bs-local.com:45691/check')

  if selenium.find_element(By.CSS_SELECTOR, 'body').text == 'Up and running':
    selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": ""}}')
  else:
    selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": ""}}')
  # selenium.quit()

  # Stop the Local instance
  bs_local.stop()