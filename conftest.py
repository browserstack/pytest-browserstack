import pytest

def pytest_addoption(parser):
  parser.addoption("-B","--browser",
    dest="browser",
    default="firefox",
    help="Browser. Valid options are firefox, ie and chrome")

@pytest.fixture
def browser():
    "pytest fixture for browser"
    return pytest.config.getoption("-B") #Note how this ties to the newly added command line parameter