from selenium import webdriver
from selenium.webdriver.common.by import By
import resources.Locators

URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"

class SignInPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.usernameLocator = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        self.passwordLocator = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        self.signInButtonLocator = self.driver.find_element(By.CSS_SELECTOR, "button[id='btnLogin']")


    def fill_username_field(self, usernameValue):
        """
        Fill the username field

        :param usernameValue: the username value to be placed on username field
        """
        self.usernameLocator.send_keys(usernameValue)

    def fill_password_field(self, passwordValue):
        """
        Fill the password field

        :param passwordValue: the password value to be placed on username field
        """
        self.passwordLocator.send_keys(passwordValue)

    def click_signIn_button(self):
        """
        Click on Sign In button for loggin

        """
        self.signInButtonLocator.click()
