import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class PetStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")
        self.wait = WebDriverWait(self.driver, 10)
        print('Browser opened')
        
        # Load configuration
        with open('config.json') as f:
            self.config = json.load(f)
        
        self.base_url = self.config['base_url']
        self.username = self.config['login']['username']
        self.password = self.config['login']['password']
        self.invalid_username = self.config['login']['invalid_username']
        self.invalid_password = self.config['login']['invalid_password']
        self.product_id_1 = 1  # Adjust as needed for testing
        self.product_id_2 = 2
        self.product_id_3 = 3 
        self.product_id_4 = 4
        self.product_id_5 = 5 # Adjust as needed for testing

    def test_peetstore_flow(self):
        driver = self.driver
        wait = self.wait

        # Open home page
        driver.get(f"{self.base_url}/")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("Welcome to our Pet Store", driver.page_source, "Home page not displayed correctly.")

       

        # Navigate to login page
        driver.get(f"{self.base_url}/login")
        time.sleep(2)  # Wait for 2 seconds

        # Test invalid login
        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
            password_field = driver.find_element(By.ID, 'password')
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            
            username_field.send_keys(self.invalid_username)
            password_field.send_keys(self.invalid_password)
            login_button.click()
            time.sleep(2)  # Wait for 2 seconds
            print('Invalid credentials verified ')
            self.assertIn("Invalid credentials", driver.page_source, "Error message not displayed for invalid credentials.")
        except Exception as e:
            self.fail(f"Invalid login form interaction failed: {e}")

        # Login with valid credentials
        driver.get(f"{self.base_url}/login")
        time.sleep(2)  # Wait for 2 seconds

        # Login
        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
            password_field = driver.find_element(By.ID, 'password')
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

            username_field.clear()
            password_field.clear()
            
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)
            login_button.click()
            time.sleep(2)  # Wait for 2 seconds
            print('valid credentials verified ')
        except Exception as e:
            self.fail(f"Login form interaction failed: {e}")

        # Verify successful login and return to home page
        try:
            wait.until(EC.url_contains(f"{self.base_url}/"))
            self.assertIn(f"Logout ({self.username})", driver.page_source, "Logout link not displayed after login.")
        except Exception as e:
            self.fail(f"Login verification failed: {e}")

         # Navigate to login page
        driver.get(f"{self.base_url}/description")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("About", driver.page_source, "About page not displayed correctly.")
        print('About page verified')

         # Open home page
        driver.get(f"{self.base_url}/")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("Welcome to our Pet Store", driver.page_source, "Home page not displayed correctly.")

         # Navigate to login page2
        driver.get(f"{self.base_url}/location")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("location", driver.page_source, "About page not displayed correctly.")
        print('Location page verified')

         # Open home page
        driver.get(f"{self.base_url}/")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("Welcome to our Pet Store", driver.page_source, "Home page not displayed correctly.")


       

        # Navigate to login page3
        driver.get(f"{self.base_url}/customer")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("location", driver.page_source, "customer reviews page not displayed correctly.")
        print('customer reviews page verified')
        

        # Open home page
        driver.get(f"{self.base_url}/")
        time.sleep(2)  # Wait for 2 seconds
        self.assertIn("Welcome to our Pet Store", driver.page_source, "Home page not displayed correctly.")

        # Add products to the cart
        try:
            add_to_cart_link_1 = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), 'Add to Cart') and contains(@href, '/add_to_cart/{self.product_id_1}')]")))
            add_to_cart_link_1.click()
            time.sleep(2)  # Wait for 2 seconds
            
            add_to_cart_link_2 = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), 'Add to Cart') and contains(@href, '/add_to_cart/{self.product_id_2}')]")))
            add_to_cart_link_2.click()
            time.sleep(2)  # Wait for 2 seconds
        except Exception as e:
            self.fail(f"Add to Cart interaction failed: {e}")

        
        # Verify successful login and return to home page
        try:
            wait.until(EC.url_contains(f"{self.base_url}/"))
            self.assertIn(f"Logout ({self.username})", driver.page_source, "Logout link not displayed after login.")
        except Exception as e:
            self.fail(f"Login verification failed: {e}")

         # Add products to the cart from the home page
        try:
            add_to_cart_link_1 = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), 'Add to Cart') and contains(@href, '/add_to_cart/{self.product_id_1}')]")))
            add_to_cart_link_1.click()
            time.sleep(2)  # Wait for 2 seconds
            
            add_to_cart_link_2 = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), 'Add to Cart') and contains(@href, '/add_to_cart/{self.product_id_2}')]")))
            add_to_cart_link_2.click()
            time.sleep(2)  # Wait for 2 seconds

            add_to_cart_link_3 = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), 'Add to Cart') and contains(@href, '/add_to_cart/{self.product_id_3}')]")))
            add_to_cart_link_3.click()
            time.sleep(2)
            print('Cart function verification')
        except Exception as e:
            self.fail(f"Add to Cart interaction failed: {e}")    

        # Open cart page and remove one product
        driver.get(f"{self.base_url}/cart")
        time.sleep(2)  # Wait for 2 seconds
        try:
            remove_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/remove_from_cart/{self.product_id_1}')]")))
            remove_button.click()
            time.sleep(2)  # Wait for 2 seconds
            print('Remove button verification')
        except Exception as e:
            self.fail(f"Remove from Cart interaction failed: {e}")

        # Checkout
        driver.get(f"{self.base_url}/checkout")
        time.sleep(2)  # Wait for 2 seconds
        try:
            # Click the "Back to Home" link on the checkout page
            back_to_home_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Back to Home')]")))
            back_to_home_link.click()
            time.sleep(2)  # Wait for 2 seconds
            print('Back to home verification')
        except Exception as e:
            # Print page source for debugging
            print("Checkout page source:\n", driver.page_source)
            self.fail(f"Checkout interaction failed: {e}")

        # Verify successful return to home page
        try:
            wait.until(EC.url_contains(f"{self.base_url}/"))
            self.assertIn("Welcome to our Pet Store", driver.page_source, "Home page not displayed after checkout.")
        except Exception as e:
            self.fail(f"Return to Home verification failed: {e}")

         # Logout
        try:
            logout_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Logout')]")))
            logout_link.click()
            time.sleep(2)  # Wait for 2 seconds
            print('Logout button verification')
        except Exception as e:
            self.fail(f"Logout interaction failed: {e}")

        # Verify successful logout
        try:
            wait.until(EC.url_contains(f"{self.base_url}/"))
            self.assertIn("Login", driver.page_source, "Login page not displayed after logout.")
        except Exception as e:
            self.fail(f"Logout verification failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
