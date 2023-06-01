import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from pageObject.WhishList import Whish_List
from pageObject import SETPassword
from selenium.webdriver.common.keys import Keys
import random

class OrdersTab(BasePage):

    Body = (By.TAG_NAME, "body")
    Dash_Board_tab = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/app-menu/div/div[1]/div/div[2]/nav/ul/li[7]")
    Orders_tab = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/app-menu/div/div[1]/div/div[2]/nav/ul/li[4]")
    Schedule_Delivery = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/ul/li[8]/a")
    Create_Schedule_Delivery = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order/div/nav/div/div[1]/button[1]")
    Confirm_TnC = (By.XPATH, "/html/body/div[4]/div/label/input")
    Continue_Button = (By.XPATH, "/html/body/div[4]/div/div[6]/button[1]")
    Part_Number = (By.NAME, "part_number")
    Select_Part = (By.XPATH, "/html/body/div[4]/div/div/div/mat-option[1]")
    Date = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[1]/div[2]/div[2]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button/span[1]")
    Next_Month = (By.XPATH, "/html/body/div[4]/div[2]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[3]")
    Datexpath = (By.XPATH, "/html/body/div[4]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[3]/td[4]/div[1]")
    Quantity = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[1]/div[2]/div[3]/div/mat-form-field/div/div[1]/div/input")
    Frequency = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[1]/div[2]/div[4]/div/mat-form-field/div/div[1]/div/input")
    Frequency_Range = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[1]/div[2]/div[5]/div/mat-form-field/div/div[1]/div/input")
    Add_Button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[1]/div[2]/div[6]/div/button")
    Confirm_add = (By.XPATH, "/html/body/modal-container/div/div/app-schedule-order-confirmation/div/div[3]/button[2]")
    Save = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order-form/div/form/div/div[3]/button")
    Confirm_save = (By.XPATH, "/html/body/div[5]/div/div[6]/button[1]")
    Select_order = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/section/mat-checkbox/label/div")
    SearchPartNo = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order/div/nav/div/div[2]/div[1]/input")
    DeleteLineItems = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/app-shedule-order/div/nav/div/div[1]/button[2]")
    Confirm_delete = (By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled.swal2-default-outline")
    Verify = (By.CSS_SELECTOR, "body > div.swal2-container.swal2-center.swal2-backdrop-show > div")

    def click_dashboard(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        self.find_element(self.Dash_Board_tab).click()

    def create_schedule_delivery(self):
        self.find_element(self.Orders_tab).click()
        time.sleep(3)
        self.find_element(self.Schedule_Delivery).click()
        self.find_element(self.Create_Schedule_Delivery).click()
        time.sleep(3)
        self.find_element(self.Confirm_TnC).click()
        self.find_element(self.Continue_Button).click()

    def add_order_details(self):
        self.find_element(self.Part_Number).send_keys("0005810058J")
        time.sleep(5)
        self.select_part()
        self.select_date()
        self.find_element(self.Quantity).send_keys("1")
        self.find_element(self.Frequency).send_keys("2")
        self.find_element(self.Frequency_Range).send_keys("1")

    def select_part(self):
        self.find_element(self.Select_Part).click()

    def select_date(self):
        self.find_element(self.Date).click()
        time.sleep(3)
        self.find_element(self.Next_Month).click()
        self.find_element(self.Datexpath).click()

    def save_schedule_order(self):
        self.find_element(self.Add_Button).send_keys(Keys.PAGE_DOWN)
        self.find_element(self.Add_Button).send_keys(Keys.ARROW_DOWN * 3)
        self.find_element(self.Add_Button).click()
        time.sleep(3)
        self.find_element(self.Confirm_add).click()
        time.sleep(3)
        self.find_element(self.Body).send_keys(Keys.PAGE_DOWN)
        self.find_element(self.Save).click()
        time.sleep(5)
        self.find_element(self.Confirm_save).click()

    def select_order(self):
        self.find_element(self.Orders_tab).click()
        time.sleep(3)
        self.find_element(self.Schedule_Delivery).click()
        self.find_element(self.SearchPartNo).send_keys("0005810058J", Keys.ENTER)
        time.sleep(3)
        self.find_element(self.Select_order).click()

    def delete_line_item(self):
        self.find_element(self.DeleteLineItems).click()
        time.sleep(5)
        self.find_element(self.Confirm_delete).click()

    def verify(self):
        v = self.find_element(self.Verify)
        y = v.text
        x = "Deleted"
        print(y)
        if x in y:
            return True
        else:
            return False
