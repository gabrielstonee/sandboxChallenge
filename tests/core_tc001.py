import pytest
from Pages.InvoiceListPage import InvoiceListPage
from Pages.SignInPage import SignInPage

def core_tc001(initial_setup):
    driver = initial_setup
    signIn_page = SignInPage(driver)
    invoiceList_page = InvoiceListPage(driver)

    try:
        print("Fill the username fields and click the button")
        signIn_page.login("demouser", "abc123")

        print("The application should redirect the user to the page Invoice List")
        if not invoiceList_page.is_page_visible():
            print(f"Esta visivel: {invoiceList_page.is_page_visible()}")
            raise Exception("User was not logged In")
    except Exception as e:
        print("Test failed with an exception")
        pytest.fail(f"Test failed with the exception: '{e}'")
    finally:
        invoiceList_page.loggout()