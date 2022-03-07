# Playwright_testing_example

This is just an example of the test automation framework using Playwright.

I am using a website that allows users to "log in" and play around for testing purposes.
The website is https://parabank.parasoft.com/

## Tests
There are 2 tests here at the moment.

The first test verifies that login was successful by checking for the visibility of text
The second test interacts with elements by clicking, and entering values.


## Setup and run

### 1. Download repo
 - Download this repo to a local directory

### 2. Venv
 - Install the Virtual Environment library using the following: pip install virtualenv
 - Create a virtual environment by runnin the command: virtualenv [directory of repo]
 - Activate the venv by running the "activate.bat" in the Scripts folder.
 - Check that the required libraries are installed (pip freeze)
 -- If not, run the following: pip install -r requirements.txt
 - Install Playwright by running the command: playwright install
 
### 3. Running tests

There are 2 ways to run the tests:

1. Pytest

To run the tests, open a command window in the venv, and run the following: **python -m pytest Playwright_tests.py --html=Playwright_tests.html**. This will kick off the tests using pytest in the Chromium browser and create a report showing the test results.

2. Unittest

To run the tests, just run the python_test_runner.py file.
This will kick off the tests and create a report showing the test results