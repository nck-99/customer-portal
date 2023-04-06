import time
import pytest
import openpyxl
from pageObject import CustomerPage
from Utilities.excel_methods import ExcelMethods

workbook = openpyxl.load_workbook('C:\Selenium\EdukaanCLogin.xlsx')

class Test_Login_Logout():
    @pytest.mark.parametrize('Test_Case_ID,Objective,Mobile_NO,Password,OTP,Condition,Expected_Results', ExcelMethods(workbook["Login"]).get_parametrize_list())
    def test_Login(self, setup, Test_Case_ID, Objective, Mobile_NO, Password, OTP, Condition, Expected_Results):
        cp = CustomerPage.LoginPage(setup)
        cp.wait(3)
        cp.select_Login()
        if Password == "-":
            if Condition == "+":
                cp.enter_mobileno(Mobile_NO)
                cp.click_send_otp()
                time.sleep(5)
                assert cp.verify_otp(setup) == True
                cp.wait(5)
                cp.enter_otp(OTP)
                cp.click_next()
                cp.select_user()
                cp.wait(5)
                if cp.verify_login() == True:
                    status = "TC PASSED"
                else:
                    status = "TC FAILED"
            elif Condition == "-":
                cp.enter_mobileno(Mobile_NO)
                cp.click_send_otp()
                time.sleep(5)
                if cp.login_error_msg(setup) == True:
                    status = "TC PASSED"
                else:
                    status = "TC FAILED"
            else:
                status = "TC FAILED"
        else :
            if Condition == "+":
                cp.enter_password(Password)
                cp.wait(5)
                cp.enter_mobileno(Mobile_NO)
                cp.sign_in()
                cp.wait(5)
                cp.select_user()
                if cp.verify_login() == True:
                    status = "TC PASSED"
                else:
                    status = "TC FAILED"
            else:
                cp.enter_password(Password)
                cp.wait(5)
                cp.enter_mobileno(Mobile_NO)
                cp.sign_in()
                cp.wait(5)
                if cp.login_error_msg(setup) == True:
                    status = "TC PASSED"
                else:
                    status = "TC FAILED"

        ExcelMethods(workbook["Login"]).update_result_in_excel(Test_Case_ID, status)
        workbook.save("C:\Selenium\EdukaanCLogin.xlsx")

    def test_Logout(self, setup):
        cp = CustomerPage.LoginPage(setup)
        cp.select_Login()
        cp.enter_mobileno("7980883043")
        cp.click_send_otp()
        cp.wait(5)
        cp.enter_otp("123456")
        cp.click_next()
        cp.select_user()
        assert cp.verify_login() == True
        time.sleep(10)
        cp.user_details()
        cp.logout()
        time.sleep(5)
        assert cp.verify_logout() == True

