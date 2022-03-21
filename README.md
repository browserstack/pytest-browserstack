# pytest-browserstack
https://browserstack.atlassian.net/wiki/spaces/PROD/pages/3358687296/Selenium+Frameworks+Documentation#Git-Repo-Names

# PyTest with Browserstack

PyTest Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* Update `.browserstack` files with your [BrowserStack Username and Access Key](https://www.browserstack.com/accounts/settings)

## Running your single tests
* To run single tests, run `pytest --driver BrowserStack --variables config/capabilities1.json`


## Running your parallel tests
* To run parallel tests, run `paver run parallel`

 Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
