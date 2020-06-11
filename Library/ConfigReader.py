import configparser

def readConfigData(section,key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/config.cfg')
#    config.read('../ConfigurationFiles/config.cfg')
    return config.get(section,key)

def fetchElementLocators(section,key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/elements.cfg')
    return config.get(section,key)

#print(readConfigData('Details','URL'))

