import time
from Utilities import utility
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


username = str(input("please enter a unique user name"))
driver = webdriver.Chrome()

driver.get("https://ibpodev.home.tatamotors/edukaan_Admin/#/pages/Login")
path = "C:\Selenium\Book1.xlsx"

rows = utility.getRowCount(path, 'Sheet1')

for r in range(2, rows):
    time.sleep(3)
    if r==2:
        username = utility.readData(path, 'Sheet1', r, 1)
        password = utility.readData(path, 'Sheet1', r, 2)
        driver.find_element(By.NAME, "name").send_keys(username)
        driver.find_element(By.NAME, "psw").send_keys(password)
driver.find_element(By.XPATH, "//*[@id='moveTop']/app-login/div/div[2]/div/form/button").click()
time.sleep(3)
if driver.title == "e-Dukaan | Dashboard":
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/app-root/app-adminlayout/app-header/header/div/div/div/ul/li[4]/a").click()
    driver.implicitly_wait(3)
    print(str(driver.title))
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/app-adminlayout/app-user-registration/section/div/button").click()
    if driver.title == "e-Dukaan | Admin User Registration":
        contractor = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[1]/ul/mat-radio-group/mat-radio-button[2]/label/div[1]/div[2]")))
        contractor.click()
        status = driver.find_element(By.XPATH, "//*[@id='mat-slide-toggle-1']/label/div/div/div[1]")
        status.click()
        dd_type = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[3]/ng-select/div/div/div[2]/input")
        dd_type.click()
        driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[3]/ng-select/ng-dropdown-panel/div/div[2]/div[1]").click()
        dd_role = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[4]/ng-select/div/div/div[2]/input")
        dd_role.click()
        driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[4]/ng-select/ng-dropdown-panel/div/div[2]/div[1]").click()
        time.sleep(3)
        fname = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[5]/input").send_keys("lesli")
        lname = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[6]/input").send_keys("chow")
        uname = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[7]/input").send_keys(username)
        phnno = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[8]/input").send_keys("9921929395")
        Email = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[2]/form/div[2]/div[9]/input").send_keys("popcon99@gmail.com")
        submit_button = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[3]/button").click()
driver.implicitly_wait(6)
save_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-new-user/div/div[3]/button[2]")))
save_button.click()
driver.implicitly_wait(5)
ok_button = driver.find_element(By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline")
assert ok_button.click(), "TC For User Registration Passed"
time.sleep(9)

