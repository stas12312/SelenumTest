from selenium import webdriver


def get_driver():
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub")
    return driver
