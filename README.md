# behavior-driven-python/pytest-bdd

### Purpose
This project shows how to do [BDD] in [Python]
using [pytest-bdd](https://github.com/pytest-dev/pytest-bdd), a plugin
for the [pytest](https://docs.pytest.org/) test automation framework and [Allure](https://allurereport.org/docs/) 
framework for generating tests reports.
It exhibits the basics of `pytest-bdd`
with simple unit- and simple e2e- tests.
Tests are meant to highlight `pytest-bdd` features,
*not* to necessarily show testing best practices for scalable solutions.
    
### Setup
This project uses
[Python 3](https://automationpanda.com/2017/02/07/which-version-of-python-should-i-use/).
Use [venv](https://docs.python.org/3/tutorial/venv.html)
to create a virtual environments for dependencies.
Use [allure](https://allurereport.org/docs/gettingstarted/installation/) to create test reports.

### Features
There is 1 feature files that showcase how to use `pytest-bdd` in various ways:

1. `book_manager.feature`
   * Contains e2e test scenarios for a bookshelf project.
   * Tests that book can be added and removed from closet.
   * Tests that new book added as unread status to closet.
   * Tests for reading books.


### Test Execution
To run all tests from the root directory, run `pytest`.
All the standard
[pytest command line options](https://docs.pytest.org/en/latest/usage.html)
work.
Use [command line options](http://behave.readthedocs.io/en/latest/behave.html)
for filtering and other controls.
Options may also be put inside the `pytest.ini`
[configuration file](https://docs.pytest.org/en/latest/reference.html#configuration-options).
Below are some common options:

```bash
# run all tests
pytest

# to understanding that markers can be use
pytest --markers


# filter tests by tags
pytest --collect-only -m "e2e" 
pytest --collect-only -m "unit"      

# print Allure report
# Replace allure-results with the path to the directory specified in the outputFolder setting of the reporter
allure serve allure-results
```
