import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class Logout_TestCase(unittest.TestCase):

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
        self.index_page()
        self.logout()

    def login_correct(self):
        # Pengujian login dengan kredensial yang benar
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def index_page(self):
        # Pengujian memastikan bahwa pengguna berhasil login
        expected_result = "admin"
        actual_result = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Halo,')]").text.split(', ')[1]
        self.assertIn(expected_result, actual_result)

    def logout(self):
        # Pengujian logout dan memeriksa apakah pengguna diarahkan kembali ke halaman login
        self.browser.find_element(By.XPATH, "//a[contains(text(),'Sign out')]").click()

        login_page_title = "Login"
        actual_title = self.browser.title
        self.assertEqual(login_page_title, actual_title)

    @classmethod
    def tearDownClass(cls):
        # Menutup browser setelah seluruh pengujian selesai
        cls.browser.quit()

if __name__ == '__main__':
    # Menjalankan unit test
    unittest.main(verbosity=2, warnings='ignore')
