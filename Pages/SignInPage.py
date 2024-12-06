from selenium import webdriver
from selenium.webdriver.common.by import By
from resources.Locators import *

class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.usernameLocator = usernameLocator
        self.passwordLocator = passwordLocator
        self.signInButtonLocator = btnLoginLocator
        self.login_errorLocator = login_errorLocator

    def fill_username_field(self, usernameValue):
        """
        Fill the username field

        :param usernameValue: the username value to be placed on username field
        """
        self.driver.find_element(By.CSS_SELECTOR, self.usernameLocator).send_keys(usernameValue)

    def fill_password_field(self, passwordValue):
        """
        Fill the password field

        :param passwordValue: the password value to be placed on password field
        """
        self.driver.find_element(By.CSS_SELECTOR, self.passwordLocator).send_keys(passwordValue)

    def click_signIn_button(self):
        """
        Click on Sign In button for loggin

        """
        self.driver.find_element(By.CSS_SELECTOR, self.signInButtonLocator).click()

    def login(self, usernameValue, passwordValue):
        """
        Login the System using the given credentials

        :param usernameValue: the username value to be placed on username field
        :param passwordValue: the password value to be placed on password field
        """
        self.fill_username_field(usernameValue)
        self.fill_password_field(passwordValue)
        self.click_signIn_button()

    def check_login_error(self):
        """
        Click if user is not able to login and receives the error Message

        """
        try:
            page_visible = self.driver.find_element(By.CSS_SELECTOR, self.login_errorLocator).is_displayed()
            return page_visible
        except:
            return False

