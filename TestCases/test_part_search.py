import time
from pageObject import PartSearch
from pageObject import SETPassword
import pytest
import openpyxl
from Utilities.excel_methods import ExcelMethods

workbook = openpyxl.load_workbook('C:\Selenium\EdukaanCLogin.xlsx')


class Test_Part_Search():
    @pytest.mark.parametrize('Test_Case_ID,Objective,Type,Data,Condition,Expected_Results', ExcelMethods(workbook["Part_Search"]).get_parametrize_list())
    def test_part_search(self, setup, Test_Case_ID, Objective, Type, Data, Condition, Expected_Results):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        ps = PartSearch.Part_Search(setup)
        ps.search_part(Data)
        time.sleep(3)
        if Condition == "+":
            if Type == "part_number":
                assert  ps.verify_part_no() == True
                status = "TC PASSED"
            elif Type == "part_description":
                assert ps.verify_part_description() == True
                status = "TC PASSED"
            elif Type == "model_name":
                assert ps.verify_model_name() == True
                status = "TC PASSED"
            elif Type == "registration_no":
                assert ps.verify_registration_no() == True
                status = "TC PASSED"
            elif Type == "chassis_no":
                assert ps.verify_chassis_no() == True
                status = "TC PASSED"
            else:
                status = "TC FAILED"
        elif Condition == "-":
            if Type == "invalid":
                assert ps.verify_empty_list() == True
                status = "TC PASSED"
            else:
                status = "TC FAILED"
        else:
            status = "TC FAILED"

        ExcelMethods(workbook["Part_Search"]).update_result_in_excel(Test_Case_ID, status)
        workbook.save("C:\Selenium\EdukaanCLogin.xlsx")