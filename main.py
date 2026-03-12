from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()

driver.get("https://www.pokemon-vortex.com/login")

time.sleep(1)

username = driver.find_element(By.NAME,"myusername")
password = driver.find_element(By.NAME,"mypassword")

username.send_keys(os.getenv("PV_USERNAME"))
password.send_keys(os.getenv("PV_PASSWORD"))
password.send_keys(Keys.RETURN)
print("Log in Succesfull !!!")

time.sleep(1)

battle_tab = driver.find_element(By.XPATH,"(//li[contains(@class,'main')])[2]")
battle_tab.click()

time.sleep(1)

battle_any_member = driver.find_element(By.XPATH,"//a[contains(.,'Battle Any Member')]")
battle_any_member.click()

time.sleep(1)

driver.execute_script("window.scrollBy(0, 300);")
fire_trainer = driver.find_element(By.XPATH,"//a[@href='/battle-user/1058571']")
fire_trainer.click()

time.sleep(1)

count=0
while True:

    try:
        rebattle = driver.find_element(By.XPATH,"//div[contains(@class,'menu-container')]//a[contains(@onclick,'/battle-user/1058571')]")
        rebattle.click()
        count+=1
        print(count + "Rounds Completed!!")
        time.sleep(2)
        continue
    except:
        pass

    driver.execute_script("window.scrollBy(0, 500);")

    try:
        attack = driver.find_element(By.XPATH,"//input[contains(@value,'Attack')]")
        attack.click()
        time.sleep(1)
        continue
    except:
        print("Attack Not Found")
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue')]")
        cont.click()
        time.sleep(1)
        print("Continue 1 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue!')]")
        cont.click()
        time.sleep(1)
        print("Continue 2 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue...')]")
        cont.click()
        time.sleep(1)
        print("Continue 3 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue..')]")
        cont.click()
        time.sleep(1)
        print("Continue 4 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue.')]")
        cont.click()
        time.sleep(1)
        print("Continue 5 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,' Continue ?')]")
        cont.click()
        time.sleep(1)
        print("Continue 6 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue ...')]")
        cont.click()
        time.sleep(1)
        print("Continue 7 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue ..')]")
        cont.click()
        time.sleep(1)
        print("Continue 8 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,' Continue ')]")
        cont.click()
        time.sleep(1)
        print("Continue 9 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,' Continue')]")
        cont.click()
        time.sleep(1)
        print("Continue 10 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue?')]")
        cont.click()
        time.sleep(1)
        print("Continue 11 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue ?')]")
        cont.click()
        time.sleep(1)
        print("Continue 12 Found")
        continue
    except:
        pass

    try:
        cont = driver.find_element(By.XPATH,"//input[contains(@value,'Continue ')]")
        cont.click()
        time.sleep(1)
        print("Continue 13 Found")
        continue
    except:
        pass


    time.sleep(0.5)