from selenium import webdriver
import unittest
from pages.pageObjects import Loginpage
import HtmlTestRunner
import time
class Employee(unittest.TestCase):

    baseUrl="https://opensource-demo.orangehrmlive.com/index.php/auth/login"
    username="Admin"
    Password="admin123"
    driver=webdriver.Chrome(executable_path="C:\\Users\\SmrutiRanjanDalei\\drivers\\chromedriver_win32 (4)\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()
        #cls.assertEqual("")

    def test_login(self):
        lp=Loginpage(self.driver)
        lp.enter_username(self.username)
        lp.enter_password(self.Password)
        lp.clickbutton()
        time.sleep(6)

    #@classmethod
    #def tearDownClass(cls):
        #cls.driver.close()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\SmrutiRanjanDalei\\PycharmProjects\\Projectt5\\reports"))
