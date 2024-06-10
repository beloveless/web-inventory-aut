# Import Library
import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfilePictureUpload_TestCase(unittest.TestCase):

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
        self.go_to_profile_page()
        self.upload_profile_picture()

    def login_correct(self):
        # Pengujian login dengan kredensial yang benar
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def go_to_profile_page(self):
        # Mengakses halaman profil
        profile_url = self.url + '/profil.php'
        self.browser.get(profile_url)

    def upload_profile_picture(self):
        # Pengujian mengunggah gambar profil
        file_input = self.browser.find_element(By.ID, 'formFile')
        
        # Menentukan path gambar yang akan diunggah
        image_path = os.path.join(os.getcwd(), 'tests', 'test_images', 'image.jpg')
        file_input.send_keys(image_path)

        # Mengklik tombol submit
        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn-secondary')
        submit_button.click()

        # Memeriksa apakah pengguna diarahkan kembali ke halaman profil
        redirected_url = self.url + '/profil.php'
        self.assertEqual(redirected_url, self.browser.current_url)

        # Memeriksa apakah gambar profil telah diperbarui
        new_profile_picture = self.browser.find_element(By.CSS_SELECTOR, 'img[src="image/profile.jpg"]')
        self.assertIsNotNone(new_profile_picture)

    @classmethod
    def tearDownClass(cls):
        # Menutup browser setelah seluruh pengujian selesai
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
