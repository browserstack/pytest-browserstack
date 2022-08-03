from ast import arg
from asyncio import tasks
from unittest import case
from paver.easy import *
from paver.setuputils import setup

setup(
    name = "pytest-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("PyTest Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-browserstack",
    packages=['tests']
)

@task
@consume_nargs(1)    
def run(args):
    """Run single, local and parallel test using different config."""
    commands = {
        "single":'pytest tests/single.py --driver BrowserStack --variables config/single.json',
        "parallel":'pytest tests/parallel.py -n 3 --driver BrowserStack --variables config/parallel.json',
        'local':'pytest tests/local/local.py --driver BrowserStack --variables config/local.json'
    }
    if commands[args[0]]:
        sh(commands[args[0]])
        
        
    
