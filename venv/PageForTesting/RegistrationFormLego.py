from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\ludmi\geckodriver')
username = driver.find_element_by_name('NAME')
useremail = driver.find_element_by_name('EMAIL')
userphone = driver.find_element_by_name('PERSONAL_PHONE')
userpassword = driver.find_element_by_name('PASSWORD')
buttonlogin = driver.find_element_by_class_name('gray-bttn')
buttonregistration = driver.find_element_by_class_name('orange-bttn')