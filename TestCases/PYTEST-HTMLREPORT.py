import pytest
from selenium import webdriver

class employee():

    @pytest.yield_fixture()
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\SmrutiRanjanDalei\\drivers\\chromedriver_win32 (4)\\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def _test_run(self,setUp):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"