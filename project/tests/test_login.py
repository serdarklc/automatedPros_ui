import unittest
from project.utils.driver_setup import setup_driver
from project.webElements.login_page import LoginPage


class TestSwagLabsLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Set up the driver once for all tests """
        cls.driver = setup_driver()
        cls.usernames = [
            "standard_user",
            "locked_out_user",
            "problem_user",
            "performance_glitch_user",
            "error_user",
            "visual_user"
        ]
        cls.password = "secret_sauce"

    def setUp(self):
        """ Runs before each test """
        self.login_page = LoginPage(self.driver)

    def test_login_with_multiple_users(self):
        """ Test case for logging in with multiple usernames """
        for username in self.usernames:
            self.login_page.enter_username(username)
            self.login_page.enter_password(self.password)
            self.login_page.click_login()

            # Validate login success or failure based on the username
            if username == "locked_out_user":
                error_message = self.login_page.get_error_message()
                self.assertEqual("Epic sadface: Sorry, this user has been locked out.", error_message)
                print(f"Login failed as expected for {username}")
            else:
                self.assertIn("inventory", self.driver.current_url, f"Login failed for {username}")
                print(f"Login successful for {username}")

            # Reset the driver to the login page for the next test
            self.driver.get("https://www.saucedemo.com/")

    @classmethod
    def tearDownClass(cls):
        """ Tear down the driver once after all tests """
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
