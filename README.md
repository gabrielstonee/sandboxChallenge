# QA Engineer Challenge: Automation Testing of sandboxChallenge
This repository stores all the testing artifacts for the validation of sandbox App
The project demonstrates automated testing of a web application using Selenium and Python

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Test Coverage](#test-coverage)
- [Running the Test Cases](#running-the-test-cases)
- [Explaining the test cases](#explaining)

## Installation
sandBox is an App resonsible for register Invoices from different users.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gabrielstonee/sandboxChallenge.git
   cd sandboxChallenge
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. It is also necessary to download the Chromedriver and add it to your path

## Technologies Used
- **Python 3.x**
- **Selenium WebDriver**
- **PyTest**
- **Git**

## Test Coverage
- **End-to-End (E2E) tests**

## Running the test cases
1. To run the tests locally, navigate to the source code of the repository and execute:
   ```bash
   pytest
   ```

2. I created a pytest.ini file to indicate which tests are up to execution. As the code is, all tests from tests path are being executed but feel free to edit accordingly

## Running the test cases

1. tc001 - This test execution was a positive path for validation. The user should be able to login successfully
During execution no problem was seen, by the given user, we were able to login successfully

2. tc002 - This test execution was a negative path for validation. The given table of users should be not be able to login and should also receive a error message
Almost every user of the given table were not logged in and also received the error message, only one of the users were able to login

3. tc003 - In This test execution the Invoice Details Information get automatically from the test, should match the one in the table. This was successfully fulfilled