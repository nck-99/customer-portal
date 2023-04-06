from selenium.webdriver.common.by import By
from BasePage.Base_Page import BasePage
from selenium.webdriver.common.keys import Keys
class Part_Search(BasePage):

    SEARCH_bar = (By.ID, "header-paste-search")
    Verify_Part_No = (By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div/h5/span")
    Verify_Part_Description = (By.CLASS_NAME, "row")
    Verify_Model_Name = (By.CLASS_NAME, "row")
    Verify_Registration_No = (By.CLASS_NAME, "prod-cat")
    Verify_Chassis_No = (By.CLASS_NAME, "prod-cat")
    Verify_No_Parts = (By.XPATH, "/html/body/div/app-root/app-main/app-header/header/div/div[2]/div[2]/form/div/div[1]/div/div[2]/div[1]/div/div")

    def search_part(self, data):
        self.find_element(self.SEARCH_bar).send_keys(data)
        self.find_element(self.SEARCH_bar).send_keys(Keys.ENTER)

    def verify_part_no(self):
        v = self.find_element(self.Verify_Part_No)
        if bool(v) == 1:
            return True
        else:
            return False

    def verify_part_description(self):
        v = self.find_all_elements(self.Verify_Part_Description)
        if len(v) != 0:
            return True
        else:
            return False

    def verify_model_name(self):
        v = self.find_all_elements(self.Verify_Model_Name)
        if len(v) != 1:
            return True
        else:
            return False

    def verify_registration_no(self):
        v = self.find_element(self.Verify_Registration_No)
        if bool(v) == 1:
            return True
        else:
            return False

    def verify_chassis_no(self):
        v = self.find_element(self.Verify_Chassis_No)
        if bool(v) == 1:
            return True
        else:
            return False

    def verify_empty_list(self):
        v = self.find_all_elements(self.Verify_No_Parts)
        if len(v) <= 1:
            return True
        else:
            return False