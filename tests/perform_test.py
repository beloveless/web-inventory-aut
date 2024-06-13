import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryWebsiteTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')  # Menjalankan browser tanpa antarmuka grafis
        cls.browser = webdriver.Firefox(options=option)

        try:
            cls.url = os.environ['URL']  # Mengambil URL dari variabel lingkungan
        except:
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

        # time.sleep(5)
        navbar_brand = WebDriverWait(self.browser, 10).until(
             EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand'))
         )
        self.assertIsNotNone(navbar_brand, "Navbar brand element should exist")
        self.assertEqual(navbar_brand.text, 'INVENTORY MANUNGGAL PERALATAN JAHIT')

    def find_button_check(self):
        admin_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
        )
        self.assertIsNotNone(admin_button, "Admin button element should exist")
        self.assertEqual(admin_button.text, 'ADMIN')

        admin_button.click()

    def login_check(self):
        access_url = 'http://' + self.url + '/login.php'
        self.browser.get(access_url)

        # time.sleep(5) 
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div/div/div[2]/form/div[1]/input'))
        ).send_keys("adminreal")
        self.browser.find_element(By.XPATH,
            '/html/body/section/div/div/div/div/div[2]/form/div[2]/input').send_keys("adminreal")
        self.browser.find_element(By.XPATH,
            '/html/body/section/div/div/div/div/div[2]/form/div[3]/input').click()

        heading_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )
        self.assertIn('SELAMAT DATANG, ADMINREAL', heading_element.text)

    def logout_check(self):
        # Pastikan pengguna sudah login sebelum mencoba logout
        self.login_check()

        # Tunggu dan klik elemen logout
        logout_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="side-menu"]/li[8]/a'))
        )
        logout_button.click()

        # Tunggu dan terima alert konfirmasi logout
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
