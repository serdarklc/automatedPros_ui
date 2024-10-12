import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from project.webElements.login_page import LoginPage
from project.webElements.inventory_page import InventoryPage
from project.utils.driver_setup import setup_driver


class TestSwagLabsInventory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Set up the driver once for all tests """
        cls.driver = setup_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.inventory_page = InventoryPage(cls.driver)

    def setUp(self):
        """ Runs before each test """
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )  # Wait for the username input to be visible
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

    def test_add_item_to_cart(self):
        """ Test case for adding an item to the cart """
        self.inventory_page.add_first_item_to_cart()
        self.assertTrue(self.inventory_page.is_item_in_cart())
        print("Item added to cart successfully!")

    def test_remove_item_from_cart(self):
        """ Test case for removing an item from the cart """
        self.inventory_page.add_first_item_to_cart()  # Add item first
        self.assertTrue(self.inventory_page.is_item_in_cart())

        self.inventory_page.remove_first_item_from_cart()
        self.assertFalse(self.inventory_page.is_item_in_cart())
        print("Item removed from cart successfully!")

    @classmethod
    def tearDownClass(cls):
        """ Tear down the driver once after all tests """
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
