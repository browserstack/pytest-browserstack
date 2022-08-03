from browserstack.local import Local
import pytest
from selenium.webdriver.common.by import By
import os
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']
bs_local = Local()

# You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
bs_local_args = { "key":  BROWSERSTACK_ACCESS_KEY if BROWSERSTACK_ACCESS_KEY else "BROWSERSTACK_ACCESS_KEY" }

def pytest_runtest_setup():
  # Starts the Local instance with the required arguments
  bs_local.start(**bs_local_args)

  # Check if BrowserStack local instance is running
  print('Check Local: ', bs_local.isRunning())

def pytest_sessionfinish(session, exitstatus):
  bs_local.stop()