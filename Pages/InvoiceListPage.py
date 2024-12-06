from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.Locators import *
import time


class InvoiceListPage:

    def __init__(self, driver):
        self.driver = driver
        self.logoutLocator = logoutLocator

    def is_page_visible(self):
        """
        Check if Invoice Lits page is visible

        """
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, self.logoutLocator)))
        return element.is_displayed()

    def loggout(self):
        """
        Loggs Out of logged Account

        """
        self.driver.find_element(By.CSS_SELECTOR, self.logoutLocator).click()

    def open_invoice_details_link(self, invoice_number):
        """
        Open Invoice Details Page by Invoice Number

        :param invoice_number: invoice number of the item to open the Invoice Details
        """
        row = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{invoice_number}')]/ancestor::div[@class='row']")

        # The hyperlink element
        invoice_link = row.find_element(By.XPATH, ".//a[@href]")
        invoice_link.click()
        time.sleep(5)
