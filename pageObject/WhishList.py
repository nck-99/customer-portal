from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class Whish_List(BasePage):

    Search_Parts = (By.ID, "header-paste-search")
    Select_Item = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div[2]/div[1]")
    Add_WhishList = (By.XPATH, "/html/body/div/app-root/app-main/section/app-productdetails/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/app-wishlist-icon/button/i")
    Whishlist = (By.XPATH, "/html/body/div[1]/app-root/app-main/app-header/header/div/div[1]/div/ul/li[3]/a/i")
    SelectAll = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[2]/mat-checkbox/label/div")
    Remove_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[2]/div/button[1]")
    Empty_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[2]/div/button[2]")
    ConfirmEmpty = (By.XPATH, "/html/body/modal-container/div/div/app-logout/div[2]/button[1]")
    MoveCart_button = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[2]/div/button[3]")
    MsgContainer = (By.ID, "toast-container")
    Container_Msg_txt = (By.XPATH, "/html/body/div[2]/div/div")
    verify_wl_item = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[2]/mat-checkbox/label/span/span[2]")
    wl_search = (By.XPATH, "/html/body/div[1]/app-root/app-main/section/app-wishlist/div/div[1]/input")


    def search_part(self, item):
        self.find_element(self.Search_Parts).send_keys(item)
        self.find_element(self.Search_Parts).send_keys(Keys.ENTER)

    def select_part(self):
        p = self.find_all_elements(self.Select_Item)
        p[0].click()

    def add_whishlist(self):
        self.find_element(self.Add_WhishList).click()

    def view_whishlist(self):
        self.find_element(self.Whishlist).click()

    def select_all(self):
        self.find_element(self.SelectAll).click()

    def remove(self):
        self.find_element(self.Remove_button).click()

    def empty_whishlist(self):
        self.find_element(self.Empty_button).click()
        self.find_element(self.ConfirmEmpty).click()

    def move_to_cart(self):
        self.find_element(self.MoveCart_button).click()

    def container_msg(self):
        msg = self.find_element(self.Container_Msg_txt).text
        return msg

    def check_msg(self):
        msg = self.find_element(self.MsgContainer)
        return bool(msg)

    def verify_whishlist_item(self):
        self.find_element(self.wl_search).send_keys("Wheel")
        time.sleep(7)
        self.find_element(self.wl_search).send_keys(Keys.ENTER)
        v = self.locate_by_visibility(self.verify_wl_item)
        if bool(v) == 1:
            return True
        else:
            return False
