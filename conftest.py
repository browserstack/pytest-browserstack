from pprint import pprint
import pytest
from browserstack.local import Local
import os, json
from jsonmerge import merge
CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

bs_local = None

BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else None

def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY or "access_key", "forcelocal": "true" }
    bs_local.start(**bs_local_args)

def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()

@pytest.fixture(scope='session')
def session_capabilities():
  desired_capabilities = merge(CONFIG['environments'][TASK_ID],CONFIG["capabilities"])
  if "local" in desired_capabilities['bstack:options'] and desired_capabilities['bstack:options']['local']:
    start_local()
  return desired_capabilities


def pytest_sessionfinish(session, exitstatus):
  stop_local()
