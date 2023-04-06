from selenium import webdriver as driver

class Login:
    txtbox_username="name"
    txtbox_password="psw"
    button_login='//*[@id="moveTop"]/app-login/div/div[2]/div/form/button'
    button_logout="/html/body/app-root/app-adminlayout/app-header/header/div/div/div/div/a/span"

    def __init__(self, driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element_by_name(self.txtbox_username).clear()
        self.driver.find_element_by_name(self.txtbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.txtbox_password).clear()
        self.driver.find_element_by_name(self.txtbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout).click()

