from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()

driver.get("https://www.pokemon-vortex.com/login")

time.sleep(2)

username = driver.find_element(By.NAME,"myusername")
password = driver.find_element(By.NAME,"mypassword")

username.send_keys(os.getenv("PV_USERNAME"))
password.send_keys(os.getenv("PV_PASSWORD"))
password.send_keys(Keys.RETURN)

time.sleep(3)

battle_tab = driver.find_element(By.XPATH,"(//li[contains(@class,'main')])[2]")
battle_tab.click()

time.sleep(2)

battle_any_member = driver.find_element(By.XPATH,"//a[contains(.,'Battle Any Member')]")
battle_any_member.click()

time.sleep(3)

fire_trainer = driver.find_element(By.XPATH,"(//table//a)[12]")
fire_trainer.click()

time.sleep(5)

while True:
    try:
        rebattle = driver.find_element(By.XPATH,"//button[contains(.,'Rebattle')]")
        rebattle.click()
        time.sleep(2)
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//button[contains(.,'Continue')]")
        cont.click()
        time.sleep(1)
        continue
    except:
        pass

    try:
        attack = driver.find_element(By.XPATH,"//button[contains(.,'Attack')]")
        attack.click()
        time.sleep(1)
        continue
    except:
        pass

    time.sleep(0.5)