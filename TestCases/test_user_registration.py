import time
import pytest
import openpyxl
from pageObject import CustomerPage
from pageObject import WhishList
from Utilities.excel_methods import ExcelMethods

workbook = openpyxl.load_workbook('C:\Selenium\EdukaanCLogin.xlsx')

class Test_User_registration:
    @pytest.mark.parametrize('Test_Case_ID,Objective,Mobile_no,Name,Addr_1,Addr_2,PIN,OTP,Password,Condition,Expected_Results', ExcelMethods(workbook["User_registration"]).get_parametrize_list())
    def test_user_registration(self, setup, Test_Case_ID, Objective, Mobile_no, Name, Addr_1, Addr_2, PIN, OTP, Password, Condition, Expected_Results):
        cp = CustomerPage.UserRegistration(setup)
        cp.click_register()
        cp.wait(7)
        if Condition == "+":
            cp.enter_new_mobileno(Mobile_no)
            cp.send_otp_button()
            cp.confirm()
            cp.enter_name(Name)
            cp.enter_address(Addr_1, Addr_2)
            cp.search_by_pincode(PIN)
            cp.submit_otp_button()
            cp.enter_OTP(OTP)
            cp.enter_pwd_and_confirm(Password)
            cp.submit_registration()
            time.sleep(15)
            assert cp.verify_login() == True
            status = "TC PASSED"
        elif Condition == "-":
            cp.enter_new_mobileno(Mobile_no)
            cp.send_otp_button()
            assert cp.login_error_msg() == True
            status = "TC PASSED"
        else:
            status = "TC FAILED"

        ExcelMethods(workbook["User_registration"]).update_result_in_excel(Test_Case_ID, status)
        workbook.save("C:\Selenium\EdukaanCLogin.xlsx")

