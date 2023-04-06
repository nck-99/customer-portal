from Utilities import utility
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://ibpodev.home.tatamotors/edukaan_Admin/#/pages/Login")
path = "C:\Selenium\Book1.xlsx"

rows = utility.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    time.sleep(3)
    username = utility.readData(path, 'Sheet1', r, 1)
    password = utility.readData(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, "name").send_keys(username)
    driver.find_element(By.NAME, "psw").send_keys(password)

    driver.find_element(By.XPATH, "//*[@id='moveTop']/app-login/div/div[2]/div/form/button").click()
    time.sleep(3)
    if driver.title == "e-Dukaan | Dashboard":
        print("TC passed")
        utility.writeData(path, 'Sheet1', r, 3, "TC Passed")
    else:
        if driver.title == "e-Dukaan | Login":
            driver.find_element(By.XPATH, "/html/body/div/div/div[6]/button[1]").click()
            utility.writeData(path, 'Sheet1', r, 3, "TC Passed")
            driver.find_element(By.NAME, "name").clear()
            driver.find_element(By.NAME, "psw").clear()
            print("TC Passed")
        else:
            print("TC Failed")
            utility.writeData(path, 'Sheet1', r, 3, "TC Failed")
    time.sleep(3)
    while driver.title == "e-Dukaan | Dashboard":
        driver.find_element(By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/div/a/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[3]/button[2]").click()
