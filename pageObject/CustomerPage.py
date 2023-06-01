import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from pageObject.WhishList import Whish_List

class LoginPage(BasePage):

    LOGIN = (By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]/img")
    OTP_radio = (By.ID, "OTP")
    PASSWORD_radio = (By.ID, "Password")
    MOBILE_NO_txtbox = (By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[1]/input")
    OTP_txtbox = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]")
    Send_OTP = (By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/button")
    PASSWORD_txtbox = (By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field[2]/div/div[1]/div[1]/input")
    NEXT_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/app-otp/section/div/mat-card/mat-card-content/form/div[2]/button[1]")
    SIGNIN = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/button")
    SELECT_FO = (By.XPATH, "/html/body/modal-container/div/div/select-user-type/div/div/div/div[2]/div/div[1]/div")
    User_ID_radio = (By.XPATH, "/html/body/modal-container/div/div/select-user/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/label")
    Confirm_User = (By.XPATH, "/html/body/modal-container/div/div/select-user/div[2]/div[2]/button")
    VERIFY = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[1]/div/ul/li[1]")
    PROFILE = (By.ID, "user-details")
    Logout_button = (By.ID, "header-logout")
    Confirm_logout = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    Login_err_msg = (By.ID, "toast-container")

    def select_Login(self):
        self.find_element(self.LOGIN).click()

    def enter_mobileno(self, mobno):
        self.find_element(self.MOBILE_NO_txtbox).send_keys(mobno)


    def enter_otp(self, otp):
        try:
            self.find_element(self.OTP_txtbox).send_keys(otp)
        except NoSuchElementException:
            pass
    def click_send_otp(self):
        self.find_element(self.Send_OTP).click()


    def enter_password(self, pwd):
        self.find_element(self.PASSWORD_radio).click()
        self.find_element(self.PASSWORD_txtbox).send_keys(pwd)

    def sign_in(self):
        self.find_element(self.SIGNIN).click()
    def click_next(self):
        self.find_element(self.NEXT_button).click()

    def select_user(self):
        self.find_element(self.SELECT_FO).click()
        time.sleep(3)
        self.find_element(self.User_ID_radio).click()
        self.find_element(self.Confirm_User).click()

    def verify_otp(self, setup):
        wl = Whish_List(setup)
        msg = wl.container_msg()
        print(msg)
        m = "OTP Sent"
        if m in msg:
            return True
        else:
            return False

    def verify_login(self):
        self.wait(3)
        v = self.find_element(self.VERIFY)
        print(v.text)
        if bool(v) == 1:
            return True
        else:
            return False
    def user_details(self):
        time.sleep(5)
        self.find_element(self.PROFILE).click()

    def logout(self):
        self.find_element(self.Logout_button).click()
        self.find_element(self.Confirm_logout).click()

    def verify_logout(self):
        v = self.locate_by_invisibility(self.VERIFY)
        if self.current_url() == "https://ibpodev.home.tatamotors/edukaan_ui/#/" and bool(v) == 1:
            return True
        else:
            return False

    def login_error_msg(self, setup):
        wl = Whish_List(setup)
        m = wl.container_msg()
        print(m)
        a = "Please enter 10 digit mobile number"
        c = "User is not registered"
        n = "Username or password do not match."
        b = "https://ibpodev.home.tatamotors/edukaan_ui/#/account/login?isLogin=true"
        self.wait(5)
        if a or c or n in m or self.driver.current_url == b:
            return True
        else:
            return False



class UserRegistration(LoginPage):

    Registration = (By.XPATH, "/html/body/div/app-root/app-main/section/app-login/section/div/mat-card/mat-card-content/form/div[2]/p[1]/a")
    MOBILE_txtbox = (By.XPATH, "/html/body/div/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/mat-form-field/div/div[1]/div[1]/input")
    SEND_OTP = (By.XPATH, "/html/body/div/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[2]/button")
    YES_button = (By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
    NAME_txtbox = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[1]/mat-form-field/div/div[1]/div/input")
    ADDR_1 = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[3]/mat-form-field/div/div[1]/div/input")
    ADDR_2 = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[4]/mat-form-field/div/div[1]/div/input")
    PIN_txtbox = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[5]/mat-form-field/div/div[1]/div[1]/input")
    SEARCH_pin = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[1]/div[5]/mat-form-field/div/div[1]/div[2]/mat-icon")
    SEND_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/section/div/mat-card/mat-card-content/form/div[2]/button")
    otp_TXTBOX = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[1]/ng-otp-input/div/input[1]")
    PWD_txtbox = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[2]/mat-form-field/div/div[1]/div[1]/input")
    Confirm_PWD = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[3]/mat-form-field/div/div[1]/div[1]/input")
    REGISTER = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-registration/app-otp/section/div/mat-card/mat-card-content/form/div[4]/button[1]")

    def click_register(self):
        self.select_Login()
        self.find_element(self.Registration).click()

    def enter_new_mobileno(self, mno):
        self.find_element(self.MOBILE_txtbox).send_keys(mno)

    def send_otp_button(self):
        self.find_element(self.SEND_OTP).click()

    def confirm(self):
        self.find_element(self.YES_button).click()


    def enter_name(self, name):
        self.find_element(self.NAME_txtbox).send_keys(name)

    def enter_address(self, addr1, addr2):
        self.find_element(self.ADDR_1).send_keys(addr1)
        self.find_element(self.ADDR_2).send_keys(addr2)

    def search_by_pincode(self, pin):
        self.find_element(self.PIN_txtbox).send_keys(pin)
        self.find_element(self.SEARCH_pin).click()

    def submit_otp_button(self):
        self.find_element(self.SEND_button).click()

    def enter_OTP(self, OTP):
        self.find_element(self.otp_TXTBOX).send_keys(OTP)

    def enter_pwd_and_confirm(self, pwd):
        self.find_element(self.PWD_txtbox).send_keys(pwd)
        self.find_element(self.Confirm_PWD).send_keys(pwd)

    def submit_registration(self):
        self.find_element(self.REGISTER).click()


