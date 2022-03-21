from browserstack.local import Local
import pytest



def test_example(selenium):
    selenium.get('https://bstackdemo.com/')

###Local testing
@pytest.fixture(autouse=True)
def run_around_tests():
    # Creates an instance of Local
    bs_local = Local()

    # You can also set an environment variable - "BROWSERSTACK_ACCESS_KEY".
    bs_local_args = { "key": "process.env.BROWSERSTACK_ACCESS_KEY" }

    # Starts the Local instance with the required arguments
    bs_local.start(**bs_local_args)

    # Check if BrowserStack local instance is running
    print('Check Local: ', bs_local.isRunning())

    yield


    # Stop the Local instance
    bs_local.stop()


def test_local(selenium):
    selenium.get('http://localhost:5500/')


