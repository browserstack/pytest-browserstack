# PyTest with Browserstack

PyTest Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by using a .browserstack configuration file in the working directory or your home directory, or by setting the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY environment variables.

## Running your single tests
* To run single tests, run `paver run single`

## Running your local tests
* To run a local test, first go to tests/local_test/conftest.py then edit BROWSERSTACK_ACCESS_KEY on line 8
* Run `paver run local`

## Running your parallel tests
* To run parallel tests, run `paver run parallel`

 Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
