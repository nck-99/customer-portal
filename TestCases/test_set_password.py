import time

import pytest
import openpyxl
from Utilities.excel_methods import ExcelMethods
from pageObject import SETPassword

workbook = openpyxl.load_workbook('C:\Selenium\EdukaanCLogin.xlsx')
class TestSetPassword():
    @pytest.mark.parametrize('Test_Case_ID,Objective,Mobile_no,Password1,Password2,Condition,Expected_Results', ExcelMethods(workbook["Set_Password"]).get_parametrize_list())
    def test_set_password(self, setup, Test_Case_ID, Objective, Mobile_no, Password1, Password2, Condition, Expected_Results):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        time.sleep(9)
        sp.click_user_profile()
        sp.set_password()
        sp.enter_password(Password1, Password2)
        sp.save()
        if Condition == "+":
            if Password1 == Password2:
                assert sp.verify_set_pw(setup, Password1, Mobile_no, Condition) == True
                status = "TC PASSED"
            else:
                status = "TC FAILED"
        elif Condition == "-":
            assert sp.verify_set_pw(setup, Password2, Mobile_no, Condition) == False
            status = "TC PASSED"
        else:
            status = "TC FAILED"

        ExcelMethods(workbook["Set_Password"]).update_result_in_excel(Test_Case_ID, status)
        workbook.save("C:\Selenium\EdukaanCLogin.xlsx")
        

