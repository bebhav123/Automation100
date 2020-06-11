from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegisterPage
import time
import pytest


#Using Page Object Model (POM)
def test_validate_registration():
    driver = InitiateDriver.startBrowser()
    register = RegisterPage.Register(driver)
    register.enter_username('Sachin')
    register.enter_pass("tendulkar")
    time.sleep(3)
    driver.close()


