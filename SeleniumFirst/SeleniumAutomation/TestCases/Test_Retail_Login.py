
from SeleniumAutomation.BaseClass.Environment import Environment as environment
from SeleniumAutomation.Pages.Retail_Login import *
from SeleniumAutomation.Pages.Home import *
from SeleniumAutomation.Utilities.Excel_Handle import *
import unittest
from ddt import *
from SeleniumAutomation.Reports import HTMLTestRunner

@ddt
class Test_Retail_Login(environment,unittest.TestCase):
    def getName(self):
        return self.__class__.__name__

    @idata(getExcelData('RetailLoginTest'))
    @unpack
    def test_retail_login(self,username,password):
        value = getExcelData()
        retail_login_page = Retail_Login(self.driver)
        retail_login_page.retail_login(username,password)
        home_page = Login(self.driver)
        home_page.verify_Login_success()












