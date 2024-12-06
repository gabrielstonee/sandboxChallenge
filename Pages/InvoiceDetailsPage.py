import time
from selenium.webdriver.common.by import By
from resources.Locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class InvoiceDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.invoiceDetailsTitleLocator = invoiceDetailsTitleLocator
        self.hotel_titleLocator = hotel_titleLocator
        self.invoice_dateLocator = invoice_dateLocator
        self.due_dateLocator = due_dateLocator
        self.booking_codeLocator = booking_codeLocator
        self.room_codeLocator = room_codeLocator
        self.total_stay_countLocator = total_stay_countLocator
        self.total_stay_amountLocator = total_stay_amountLocator
        self.check_inLocator = check_inLocator
        self.check_outLocator = check_outLocator
        self.invoice_numberDetailsLocator = invoice_numberDetailsLocator
        self.deposit_nowtLocator = deposit_nowtLocator
        self.tax_vatLocator = tax_vatLocator
        self.total_amountLocator = total_amountLocator
        self.customer_detailsLocator = customer_detailsLocator

    def is_page_visible(self):
        """
        Check if Invoice Details page is visible

        """
        try:
            page_visible = self.driver.find_element(By.XPATH, self.invoiceDetailsTitleLocator).is_displayed()
            return page_visible
        except:
            return False

    def get_hotel_name(self):
        """
        Get Hotel name information

        :return: Hotel Name
        """
        time.sleep(10)
        return self.driver.find_element(By.XPATH, self.hotel_titleLocator).text

    def get_invoice_date(self):
        """
        Get Invoice Date information

        :return: Invoice Date
        """
        invoice_date = self.driver.find_element(By.XPATH, self.invoice_dateLocator).text
        invoice_date = invoice_date.split(" ")[2]
        return invoice_date

    def get_due_date(self):
        """
        Get Due Date information

        :return: Due Date
        """
        due_date = self.driver.find_element(By.XPATH, self.due_dateLocator).text
        due_date = due_date.split(" ")[2]
        return due_date

    def get_booking_code(self):
        """
        Get Booking Code information

        :return: Booking code
        """
        return self.driver.find_element(By.XPATH, self.booking_codeLocator).text

    def get_room(self):
        """
        Get Room information

        :return: Room code
        """
        return self.driver.find_element(By.XPATH, self.room_codeLocator).text

    def get_stay_count(self):
        """
        Get Total Stay Count information

        :return: Total Stay Count
        """
        return self.driver.find_element(By.XPATH, self.total_stay_countLocator).text

    def get_stay_amount(self):
        """
        Get Total Stay Ammount information

        :return: Total Stay Ammount
        """
        return self.driver.find_element(By.XPATH, self.total_stay_amountLocator).text

    def get_check_in(self):
        """
        Get Check In information

        :return: Check-In date
        """
        return self.driver.find_element(By.XPATH, self.check_inLocator).text

    def get_check_out(self):
        """
        Get Check Out information

        :return: Check-Out date
        """
        return self.driver.find_element(By.XPATH, self.check_outLocator).text

    def get_invoice_number(self):
        """
        Get Invoice Number information

        :return: Invoice Number
        """
        invoice_number = self.driver.find_element(By.CSS_SELECTOR, self.invoice_numberDetailsLocator).text
        invoice_number = invoice_number.split(" ")[1][1:]
        return invoice_number

    def get_deposit_nowt(self):
        """
        Get Deposit information

        :return: Deposit information
        """
        return self.driver.find_element(By.XPATH, self.deposit_nowtLocator).text

    def get_tax_vat(self):
        """
        Get Tax and VAT information

        :return: Tax and VAT
        """
        return self.driver.find_element(By.XPATH, self.tax_vatLocator).text

    def get_total_amount(self):
        """
        Get Total Amount information

        :return: Total Amount
        """
        return self.driver.find_element(By.XPATH, self.total_amountLocator).text

    def get_customer_details(self):
        """
        Get Customar Details information

        :return: Customer Details Information
        """
        return self.driver.find_element(By.XPATH, self.customer_detailsLocator).text

    def get_invoice_details_info(self):
        """
        Get all Invoice Details information

        :return: Invoice Details Information
        """
        invoice_details = [
            self.get_hotel_name(),
            self.get_invoice_date(),
            self.get_due_date(),
            self.get_invoice_number(),
            self.get_booking_code(),
            self.get_customer_details(),
            self.get_room(),
            self.get_check_in(),
            self.get_check_out(),
            self.get_stay_count(),
            self.get_stay_amount(),
            self.get_deposit_nowt(),
            self.get_tax_vat(),
            self.get_total_amount()
        ]
        return invoice_details