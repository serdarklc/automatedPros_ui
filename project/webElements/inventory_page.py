from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    # Web Elements
    first_item_add_to_cart = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    first_item_remove_from_cart = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")

    # Actions
    def add_first_item_to_cart(self):
        self.driver.find_element(*self.first_item_add_to_cart).click()

    def remove_first_item_from_cart(self):
        self.driver.find_element(*self.first_item_remove_from_cart).click()

    def is_item_in_cart(self):
        return len(self.driver.find_elements(*self.cart_badge)) > 0
