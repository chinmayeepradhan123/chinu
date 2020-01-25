from locators.Element_locators import locators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class Loginpage():
# loginpage locators
 username_textbox_id = locators.username_textbox_id
 password_textbox_id = locators.password_textbox_id
 click_button_id = locators.click_button_id

# homepage locators
 admin_mousehover_id = locators.admin_mousehover_id
 admin_uermg_mouse_id = locators.admin_uermg_mouse_id
 admin_users_id = locators.admin_users_id



 def __init__(self,driver):
       self.driver=driver
 def enter_username(self,username):
       self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
 def enter_password(self,password):
       self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
 def clickbutton(self):
       self.driver.find_element_by_id(self.click_button_id).click()
 def admin1(self):
       self.driver.find_element_by_id(self.admin_mousehover_id)
 def adminuser(self):
       self.driver.find_element_by_id(self.admin_uermg_mouse_id)
 def adminuser1(self):
       self.driver.find_element_by_id(self.admin_users_id)

