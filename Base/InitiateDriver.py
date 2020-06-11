from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

def startBrowser():
    global driver

    if(ConfigReader.readConfigData('Details','BROWSER')=="chrome") :
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get(ConfigReader.readConfigData('Details','URL'))
        driver.maximize_window()
        return driver

    elif(ConfigReader.readConfigData('Details','BROWSER')=="firefox") :
        path = "./Driver/geckodriver.exe"
        driver = Firefox(executable_path=path)
        driver.maximize_window()
        driver.get(ConfigReader.readConfigData('Details', 'URL'))
        return driver
    else :
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get(ConfigReader.readConfigData('Details', 'URL'))
        driver.maximize_window()
        return driver


def closeBrowser():
    driver.close()
