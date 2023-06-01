import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from pageObject.CustomerPage import LoginPage

class SetPassword(BasePage):
        UserProfile = (By.ID, "user-details")
        SetPwd = (By.ID, "header-password")
        Password_txtbox = (By.ID, "checkout-Shop-name")
        Confirm_pwd_txtbox = (By.ID, "checkout-address")
        SAVE_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/set-password/div/div/div/div/div/div/div/div/form/div/button")
        VERIFY_container = (By.ID, "toast-container")
        Skip_Tour = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-coach-marks/div/div/div[4]/button[1]")
        def click_user_profile(self):
            self.find_element(self.UserProfile).click()

        def set_password(self):
            self.find_element(self.SetPwd).click()

        def enter_password(self, pwd1, pwd2):
            self.find_element(self.Password_txtbox).send_keys(pwd1)
            self.find_element(self.Confirm_pwd_txtbox).send_keys(pwd2)

        def save(self):
            self.find_element(self.SAVE_button).click()

        def skip_tour(self):
            self.find_element(self.Skip_Tour).click()

        def verify_set_pw(self, setup, pw, mno, con):
            cp = LoginPage(setup)
            cp.user_details()
            cp.logout()
            time.sleep(5)
            cp.select_Login()
            cp.enter_mobileno(mno)
            cp.enter_password(pw)
            cp.sign_in()
            if con == "+":
                time.sleep(5)
                cp.select_user()
            else:
                pass
            time.sleep(3)
            if cp.current_url() == "https://ibpodev.home.tatamotors/edukaan_ui/#/" and cp.verify_login() == True:
                return True
            else:
                return False

        def static_login(self, setup):
            cp = LoginPage(setup)
            cp.select_Login()
            cp.enter_mobileno("7980883043")
            cp.click_send_otp()
            cp.wait(3)
            cp.enter_otp("123456")
            cp.click_next()
            time.sleep(3)
            cp.select_user()
            cp.wait(5)
            self.skip_tour()






