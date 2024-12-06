import pytest
from Pages.InvoiceListPage import InvoiceListPage
from Pages.InvoiceDetailsPage import InvoiceDetailsPage
from resources.Data import *
from resources.utils_lib import switch_window, check_elements_from_invoice_list

def core_tc003(initial_setup, user_logged):
    driver = initial_setup
    invoiceList_page = InvoiceListPage(driver)
    invoiceDetails_page = InvoiceDetailsPage(driver)
    current_window_handle = driver.current_window_handle

    try:
        print("Click the Invoice Details link for the first item presented in the screen.")
        invoiceList_page.open_invoice_details_link("110")
        switch_window(driver, current_window_handle)

        print("The application opens the Invoice Details Screen")
        if not invoiceDetails_page.is_page_visible():
            raise Exception("Invoice Details Page was not opened")

        print("Validate the information presented")
        actual_invoice_list = invoiceDetails_page.get_invoice_details_info()
        expected_invoice_list = tc003[0]
        incorrect_elements = check_elements_from_invoice_list(expected_invoice_list, actual_invoice_list)
        if incorrect_elements:
            raise Exception(f"The Invoice Details Information does not match with the expected values. \nValues that are not accordingly: {incorrect_elements}")

    except Exception as e:
        print("Test failed with an exception")
        pytest.fail(f"Test failed with the exception: '{e}'")

