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

def run_py_test(config):
    sh('pytest tests/%s.py --driver BrowserStack --variables config/%s.json' % (config,config))

@task
@consume_nargs(1)    
def run(args):
    """Run single, local and parallel test using different config."""
    if args[0] in ('single', 'parallel'):
        run_py_test(args[0])
    elif args[0] == 'local':
        sh('pytest tests/local/local.py --driver BrowserStack --variables config/local.json')
        
    
