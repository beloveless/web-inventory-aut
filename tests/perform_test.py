import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InventoryWebsiteTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')  # Menjalankan browser tanpa antarmuka grafis
        cls.browser = webdriver.Firefox(options=option)

        try:
            cls.url = os.environ['URL']  # Mengambil URL dari variabel lingkungan
        except KeyError:
            cls.url = "http://localhost"
    
    def take_screenshot(self, test_name):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
        self.browser.save_screenshot(screenshot_path)

    def test(self):
        # Menjalankan serangkaian pengujian
        self.page_heading_check()
        self.find_button_check()
        self.login_check()

    def page_heading_check(self):
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        try:
            navbar_brand = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand'))
            )
            self.assertIsNotNone(navbar_brand, "Navbar brand element should exist")
            self.assertEqual(navbar_brand.text, 'INVENTORY MANUNGGAL PERALATAN JAHIT')
        except Exception as e:
            self.take_screenshot("page_heading_check")
            raise e

    def find_button_check(self):
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        try:
            admin_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
            )
            self.assertIsNotNone(admin_button, "Admin button element should exist")
            self.assertEqual(admin_button.text, 'ADMIN')

            admin_button.click()
            time.sleep(15)
        except Exception as e:
            self.take_screenshot("find_button_check")
            raise e

    def login_check(self):
        access_url = 'http://' + self.url + '/admin/login.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        try:
            username_field = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, 'user'))
            )
            username_field.send_keys("adminreal")
            self.take_screenshot("login_check_username")
        except Exception as e:
            raise e

        try:
            password_field = self.browser.find_element(By.NAME, 'pass')
            password_field.send_keys("adminreal")
            self.take_screenshot("login_check_password")
        except Exception as e:
            raise e

        try:
            self.take_screenshot("login_check_submit0")
            submit_button = self.browser.find_element(By.XPATH,
                '/html/body/section/div/div/div/div/div[2]/form/div[3]/input')
            submit_button.click()
            self.take_screenshot("login_check_submit")
        except Exception as e:
            raise e

        try:
            heading_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )
            self.assertIn('SELAMAT DATANG, ADMINREAL', heading_element.text)
            self.take_screenshot("login_check_heading1")
        except Exception as e:
            self.take_screenshot("login_check_heading")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
