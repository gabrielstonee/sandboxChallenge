import pytest
from selenium import webdriver
from Pages.SignInPage import SignInPage


@pytest.fixture
def initial_setup():
    driver = webdriver.Chrome()
    driver.get("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user_logged(initial_setup):
     """
     Log user before test execution

     :param initial_setup: reference to initial setup fxture responsible for returning the driver instance
     """
     signIn_page = SignInPage(initial_setup)
     signIn_page.login("demouser", "abc123")
     return initial_setup