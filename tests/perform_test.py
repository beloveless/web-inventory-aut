import unittest
import os
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

    def test(self):
        # Menjalankan serangkaian pengujian
        self.page_heading_check()
        self.find_button_check()
        self.login_check()
        self.logout_check()

    def page_heading_check(self):
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        navbar_brand = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand'))
        )
        self.assertIsNotNone(navbar_brand, "Navbar brand element should exist")
        self.assertEqual(navbar_brand.text, 'INVENTORY MANUNGGAL PERALATAN JAHIT')

    def find_button_check(self):
        access_url = 'http://' + self.url + '/index.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        admin_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
        )
        self.assertIsNotNone(admin_button, "Admin button element should exist")
        self.assertEqual(admin_button.text, 'ADMIN')

        admin_button.click()

    def login_check(self):
        access_url = 'http://' + self.url + '/login.php'
        self.browser.get(access_url)
        print(f"Accessing URL: {access_url}")

        try:
            username_field = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div/div/div[2]/form/div[1]/input'))
            )
            username_field.send_keys("adminreal")
        except TimeoutException:
            print("Error finding username field: TimeoutException")
            self.fail("Failed to find username field")
        except Exception as e:
            print(f"Error finding username field: {e}")
            self.fail("Failed to find username field")

        try:
            password_field = self.browser.find_element(By.XPATH,
                '/html/body/section/div/div/div/div/div[2]/form/div[2]/input')
            password_field.send_keys("adminreal")
        except TimeoutException:
            print("Error finding password field: TimeoutException")
            self.fail("Failed to find password field")
        except Exception as e:
            print(f"Error finding password field: {e}")
            self.fail("Failed to find password field")

        try:
            submit_button = self.browser.find_element(By.XPATH,
                '/html/body/section/div/div/div/div/div[2]/form/div[3]/input')
            submit_button.click()
        except TimeoutException:
            print("Error finding submit button: TimeoutException")
            self.fail("Failed to find submit button")
        except Exception as e:
            print(f"Error finding submit button: {e}")
            self.fail("Failed to find submit button")

        try:
            heading_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'h1'))
            )
            self.assertIn('SELAMAT DATANG, ADMINREAL', heading_element.text)
        except TimeoutException:
            print("Error finding heading element: TimeoutException")
            self.fail("Failed to find heading element")
        except Exception as e:
            print(f"Error finding heading element: {e}")
            self.fail("Failed to find heading element")

    def logout_check(self):
        # Pastikan pengguna sudah login sebelum mencoba logout
        self.login_check()

        # Tunggu dan klik elemen logout
        try:
            logout_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[8]/a'))
            )
            logout_button.click()
        except TimeoutException:
            print("Error finding logout button: TimeoutException")
            self.fail("Failed to find logout button")
        except Exception as e:
            print(f"Error finding logout button: {e}")
            self.fail("Failed to find logout button")

        # Tunggu dan terima alert konfirmasi logout
        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("Error handling logout alert: TimeoutException")
            self.fail("Failed to handle logout alert")
        except Exception as e:
            print(f"Error handling logout alert: {e}")
            self.fail("Failed to handle logout alert")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
