import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class XSS_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inisialisasi pengaturan untuk browser Firefox
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')  # Menjalankan browser tanpa antarmuka grafis
        cls.browser = webdriver.Firefox(options=option)

        # Memeriksa apakah variabel lingkungan 'URL' ada dan memiliki nilai
        cls.url = os.getenv('URL', 'http://localhost')

        # Memastikan bahwa URL memiliki protokol 'http://' jika tidak ada
        if not cls.url.startswith('http'):
            cls.url = 'http://' + cls.url

    def test(self):
        # Menjalankan serangkaian pengujian
        self.login_correct()
        self.xss_page()

    def login_correct(self):
        # Pengujian login dengan kredensial yang benar
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def xss_page(self):
        # Pengujian deteksi XSS pada halaman khusus XSS
        xss_url = self.url + '/xss.php'
        self.browser.get(xss_url)

        input_field = self.browser.find_element(By.NAME, 'thing')

        # Menyuntikkan payload XSS
        input_value = '<script>alert("XSS Attack!");</script>'
        input_field.send_keys(input_value)

        submit_button = self.browser.find_element(By.NAME, 'submit')
        submit_button.click()

        # Memeriksa apakah alert XSS muncul
        alert = self.browser.switch_to.alert
        self.assertEqual('XSS Attack!', alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        # Menutup browser setelah seluruh pengujian selesai
        cls.browser.quit()

if __name__ == 'main':
    # Menjalankan unit test
    unittest.main(verbosity=2, warnings='ignore')
