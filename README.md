# PyTest with Browserstack

PyTest Integration with BrowserStack using SDK.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
## Prerequisite
* Python3

## Setup

* Clone the repo with `git clone -b sdk https://github.com/browserstack/pytest-browserstack.git`
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac
  env\Scripts\activate # on Windows
  ```
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by providing your username and access key in the `browserstack.yml` configuration file, or by setting the `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables.

## Run sample test in parallel:
* To run the sample test across platforms defined in the configuration file run:
```
  browserstack-sdk pytest -s tests/bstack-sample-test.py
```

## Run a sample local test:
* To run the sample local test across platforms defined in the configuration file, you just need to set `browserstackLocal` key as true in the `browserstack.yml` file and run:
```
  browserstack-sdk pytest -s tests/bstack-local-test.py
```

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
