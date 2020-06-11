from Base import InitiateDriver
from Pages import RegisterPage
from DataGenerate import DataGen
import time
import pytest


#Using Page Object Model (POM)
@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_validate_registration(data):
    driver = InitiateDriver.startBrowser()
    register = RegisterPage.Register(driver)
    register.enter_username(data[0])
    register.enter_pass(data[1])
    time.sleep(1)
    driver.close()
