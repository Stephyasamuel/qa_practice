from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("PASSWORD")
email=os.getenv("EMAIL")

def test_registration():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com")
    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
    driver.find_element(By.XPATH,"//*[@id='gender-female']").click()
    driver.find_element(By.NAME,'FirstName').send_keys("Stephy")
    driver.find_element(By.NAME,'LastName').send_keys("Samuel")
    driver.find_element(By.NAME,"Email").send_keys(email)
    driver.find_element(By.NAME,"Password").send_keys(password)
    driver.find_element(By.NAME,"Password").send_keys(password)
    driver.find_element(By.ID,"register-button").click()
    
    driver.quit()
