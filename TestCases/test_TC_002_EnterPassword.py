from Base import InitiateDriver
from Library import ConfigReader
import time

def test_enter_password():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name(ConfigReader.fetchElementLocators('Registration','password')).send_keys('abc')
    time.sleep(3)
    InitiateDriver.closeBrowser()