import time
from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage

from pageObject import SETPassword
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Orders(BasePage):
    Body = (By.TAG_NAME, "body")
    Part_Search = (By.ID, "header-paste-search")
    User_Details = (By.ID, "user-details")
    Add_Cart = (By.XPATH, "/html/body/div/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
    Cart = (By.ID, "cart-details")
    Clear  = (By.CLASS_NAME, "clear")
    Clear_All = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/div[2]/div/p[3]/span")
    Confirm_Clear = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    View_Cart = (By.ID, "view-all-items")
    Order_History = (By.ID, "header-order-history")
    Search_OTC = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/div/ecom-orders/div/nav/div/div/div[1]/input")
    Verify_empty_cart = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div")
    Next_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[4]/mat-card/div[3]/button")
    Proceed_to_payment = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-address/div/form/fieldset/div/div[2]/mat-card/div[5]/button[2]")
    Apply_cupon = (By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
    GST_popup = (By.XPATH, "/html/body/modal-container/div/div/gst-permmission/div/div/div[2]/button[2]")
    Terms_Conditions = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-payment/div/form/fieldset/div/div[2]/mat-card/div[5]/mat-checkbox/label/div")
    Place_Order = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-payment/div/form/fieldset/div/div[2]/mat-card/div[6]/button[2]")
    Credit = (By.ID, "type2")
    Confirm_Credit = (By.XPATH, "/html/body/div[3]/div/div[6]/button[1]")
    Order_no = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/order-confirmation/div/div[2]/div[2]/div/div[2]/h6")
    Temporary_Orders = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-layout/div/div/div/ul[1]/li[7]")
    Cancel_Order = (By.LINK_TEXT, "Cancel Order")
    select_cancel_order_id = (By.ID, "allSelected")
    select_reason = (By.ID, "checkout-state")
    submit_cancel_req = (By.XPATH, "/html/body/modal-container/div/div/order-details/div[2]/div/div[4]/div[4]/div/button")
    confirm_cancel_req = (By.XPATH, "/html/body/modal-container[2]/div/div/app-logout/div[2]/button[1]")

    def add_to_cart(self, setup, item):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part(item)
        wl.select_part()
        self.driver.execute_script("window.scrollTo(0, 100);")
        self.find_element(self.Add_Cart).click()
        time.sleep(3)

    def verify_add_cart(self, setup):
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        print("########", msg)
        a = "added to cart"
        b = "Product already exist."
        if a in msg:
            return True
        elif b in msg:
            return True
        else:
            return False

    def remove_from_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        time.sleep(5)
        self.find_element(self.Cart).click()
        time.sleep(5)
        clr = self.find_all_elements(self.Clear)
        try:
            for c in clr:
                c.click()
                time.sleep(5)
        except :
            raise "Existing items in cart."

    def verify_remove_cart(self):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        time.sleep(3)
        msg = self.find_element(self.Verify_empty_cart).text
        print(msg)
        check = "shopping cart is empty"
        if check in msg:
            return  True
        else:
            return False

    def empty_cart(self, setup):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        time.sleep(3)
        self.find_element(self.Clear_All).click()
        self.find_element(self.Confirm_Clear).click()
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        if "Cleared all cart successfully" in msg:
            return True
        else:
            return False

    def place_order(self, setup):
        self.find_element(self.Cart).click()
        self.find_element(self.View_Cart).click()
        self.wait(4)
        order = self.find_element(self.Next_button)
        order.send_keys(Keys.ARROW_DOWN * 10)
        time.sleep(3)
        order.click()

    def apply_cupon(self):
        try:
            cupon = self.find_element(self.Apply_cupon)
            cupon.click()
        except NoSuchElementException:
            pass

    def move_to_payment(self):
        self.find_element(self.Proceed_to_payment).send_keys(Keys.ARROW_DOWN * 10)
        time.sleep(3)
        self.find_element(self.Proceed_to_payment).click()
        time.sleep(3)
        self.find_element(self.GST_popup).click()
        time.sleep(3)
        self.find_element(self.Body).send_keys(Keys.ARROW_DOWN * 15)
        time.sleep(3)
        self.find_element(self.Credit).click()
        time.sleep(5)
        self.find_element(self.Confirm_Credit).click()
        time.sleep(3)
        self.find_element(self.Terms_Conditions).click()
        self.find_element(self.Place_Order).click()
        time.sleep(10)

    def verify_order_no(self):
        order_no = self.find_element(self.Order_no)
        print(order_no)
        print(order_no.text)
        return order_no.text

    def cancel_order(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        self.find_element(self.User_Details).click()
        time.sleep(3)
        self.find_element(self.Order_History).click()
        time.sleep(3)
        self.find_element(self.Temporary_Orders).click()
        time.sleep(3)
        self.find_element(self.Cancel_Order).click()
        self.find_element(self.select_cancel_order_id).click()
        reason = self.find_element(self.select_reason)
        reason.send_keys("W")
        reason.click()
        self.find_element(self.submit_cancel_req).click()
        self.find_element(self.confirm_cancel_req).click()

    def verify_cancel_order(self, setup):
        wl = WhishList.Whish_List(setup)
        msg = wl.container_msg()
        m = "Cancellation Request Accepted"
        if m in msg:
            return True
        else:
            return False