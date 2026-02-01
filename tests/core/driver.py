from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    options = Options()
    options.add_argument("--no-sandbox")  # Обязательно для CI!
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
    driver = webdriver.Chrome(options=options)
    return driver
