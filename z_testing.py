from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()
sleep(5)
driver.find_element(By.XPATH , '//*[@id="inputUsername"]' ).send_keys( 'admin' )
driver.find_element(By.XPATH , '//*[@id="inputPassword"]' ).send_keys( 'admin@123' )
driver.find_element(By.XPATH , '/html/body/div/div/div/form/div[2]/input' ).click()
sleep(10)

driver.close()
