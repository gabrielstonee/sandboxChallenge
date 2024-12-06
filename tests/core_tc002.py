import pytest
from Pages.SignInPage import SignInPage
from Pages.InvoiceListPage import InvoiceListPage
from resources.Data import *

def core_tc002(initial_setup):
    driver = initial_setup
    signIn_page = SignInPage(driver)
    failures = {}

    for iteration, (username, password) in enumerate(tc002, start=1):
        try:
            print("Start Iteration {iteration}:")
            print(f"[Iteration {iteration}] -  Fill the {username} and password fields and click the button")
            signIn_page.login(username, password)

            print("[Iteration {iteration}] - The application should show the message 'Wrong username or password'")
            if not signIn_page.check_login_error():
                raise Exception("User did not receive the Error Message")
        except Exception as e:
            print("[Iteration {iteration}] - [{username}] Iteration Failed")
            failures[iteration] = e

        assert len(failures) == 0, f"Test failed in {len(failures)} iterations: {failures}"

