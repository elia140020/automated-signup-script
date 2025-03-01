import time
import csv
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://forms.app/auth/signup#withemail")
time.sleep(3)

# 📂 Read data from CSV file
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header of the CSV file
    for row in reader:
        fullname, email, username, password = row  # value in the CSV

        # Open a new tab for each registration
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])  # switch a new tab  

        # Go to the registration page in a new tab
        driver.get("https://forms.app/auth/signup#withemail")
        time.sleep(3)

    
        # Fill the fields in the new tab
        Fullname = driver.find_element(By.XPATH, "//input[@name='full-name']")
        Fullname.send_keys(fullname)

        Email = driver.find_element(By.XPATH, "//input[@name='email']")
        Email.send_keys(email)

        Username = driver.find_element(By.XPATH, "//input[@name='username']")
        Username.send_keys(username)

        Password = driver.find_element(By.XPATH, "//input[@name='password']")
        Password.send_keys(password)

        time.sleep(1)

        check_box = driver.find_element(By.XPATH, "//i[@class='before-checkbox']")
        check_box.click()

        time.sleep(1)

        sign_up = driver.find_element(By.XPATH, "//div[@class='i-button auth-button']")
        sign_up.click()

        time.sleep(8)  #Wite for Register 

driver.quit()
