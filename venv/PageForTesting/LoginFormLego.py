from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\ludmi\geckodriver')
userlogin = driver.find_element_by_name('USER_LOGIN')
userpass = driver.find_element_by_name('pass-oneclick')
rememberme = driver.find_element_by_name('USER_REMEMBER')
forgotpass = driver.find_element_by_link_text('Забыли пароль?')
buttonlogin = driver.find_element_by_class_name('orange-bttn')
buttonregistration = driver.find_element_by_class_name('gray-bttn')