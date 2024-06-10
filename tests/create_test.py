# Import Library
import unittest
import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CreateContact_TestCase(unittest.TestCase):

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

        cls.name_query = ''.join(random.choices(string.ascii_letters, k=10))  # Membuat string acak untuk nama kontak

    def test(self):
        # Menjalankan serangkaian pengujian
        self.login_correct_credentials()
        self.create_contact()
        self.search_contact()
        self.delete_contact()

    def login_correct_credentials(self):
        # Pengujian login dengan kredensial yang benar
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def create_contact(self):
        # Pengujian membuat kontak baru
        create_url = self.url + '/create.php'
        self.browser.get(create_url)

        # Mengisi form pembuatan kontak
        self.browser.find_element(By.ID, 'name').send_keys(self.name_query)
        self.browser.find_element(By.ID, 'email').send_keys('test@example.com')
        self.browser.find_element(By.ID, 'phone').send_keys('1234567890')
        self.browser.find_element(By.ID, 'title').send_keys('Developer')

        # Mengklik tombol submit
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        # Memverifikasi halaman tujuan setelah pembuatan kontak
        index_page_title = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(index_page_title, actual_title)

    def search_contact(self):
        # Pengujian pencarian kontak
        search_query = self.name_query
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(search_query)
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

        # Memeriksa apakah kontak yang dicari ada
        searched_contact_name = self.name_query
        searched_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{searched_contact_name}')]")
        self.assertTrue(searched_contact_exists)

    def delete_contact(self):
        # Pengujian menghapus kontak
        actions_section = self.browser.find_element(By.XPATH, "//tr[@role='row'][1]//td[contains(@class, 'actions')]")
        delete_button = actions_section.find_element(By.XPATH, ".//a[contains(@class, 'btn-danger')]")

        # Mengklik tombol hapus
        delete_button.click()

        # Menyetujui konfirmasi penghapusan
        self.browser.switch_to.alert.accept()
        time.sleep(3)

        # Melakukan pencarian kembali dan memeriksa apakah kontak sudah dihapus
        search_query = self.name_query
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(search_query)
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

        searched_contact_name = self.name_query
        searched_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{searched_contact_name}')]")
        self.assertFalse(searched_contact_exists)

    @classmethod
    def tearDownClass(cls):
        # Menutup browser setelah seluruh pengujian selesai
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
