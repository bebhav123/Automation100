from Library import ConfigReader


class Register:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self,uname):
        driver.find_element_by_name(ConfigReader.fetchElementLocators('Registration','username')).send_keys(uname)

    def enter_pass(self,password):
        driver.find_element_by_name(ConfigReader.fetchElementLocators('Registration', 'password')).send_keys(password)