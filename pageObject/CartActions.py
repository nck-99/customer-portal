from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage

class Cart_Actions(BasePage):

    CartDetails = (By.ID, "cart-details")
    ViewItems = (By.ID, "view-all-items")
    AddCart = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/a")
    ClearCart = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/div[2]/div/p[3]/span")
    ClearConfirm = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    Verify = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/cart-summary/div/form/fieldset/div/div[3]/mat-card/mat-tab-group/div/mat-tab-body[1]/div/div/div/table/thead/tr/th[1]/mat-checkbox/label/div")

    def view_cart(self):
        self.find_element(self.CartDetails).click()
        self.find_element(self.ViewItems).click()

    def add_to_cart(self):
        self.find_element(self.AddCart).click()

    def clear_cart(self):
        self.find_element(self.ClearCart).click()
        self.find_element(self.ClearConfirm).click()

    def Verify_cart_item(self):
        v = self.locate_by_visibility(self.Verify)
        if bool(v) == 1:
            return True
        else:
            return False