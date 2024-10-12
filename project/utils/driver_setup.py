from selenium import webdriver

def setup_driver():
    driver = webdriver.Chrome()  # Use the correct WebDriver
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    return driver
