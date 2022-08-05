import pytest
from selenium.webdriver.common.by import By

def test_local(selenium):
  selenium.get('http://bs-local.com:45691/check')

  if selenium.find_element(By.CSS_SELECTOR, 'body').text == 'Up and running':
    selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Local is Running"}}')
  else:
    selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Local is Not Running"}}')