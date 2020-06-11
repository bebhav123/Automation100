from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegisterPage
import time
import pytest

def dataGenerator():
    li = [['uname1','pass1'],['uname2','pass2'],['uname3','pass3']]
    return li

#Using Page Object Model (POM)
@pytest.mark.parametrize('data',dataGenerator())
def test_validate_registration(data):
    driver = InitiateDriver.startBrowser()
    register = RegisterPage.Register(driver)
    register.enter_username(data[0])
    register.enter_pass(data[1])
    time.sleep(2)
    driver.close()


