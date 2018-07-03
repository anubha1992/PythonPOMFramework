from selenium import webdriver
from SeleniumAutomation.Utilities.Functions import Functions
from selenium.webdriver.common.by import By
from  SeleniumAutomation.Pages.Home import Login
from  SeleniumAutomation.Pages.Retail_Page_Locator import *
from  SeleniumAutomation.Pages.Home_Locator import *

class Retail_Login():

    def __init__(self,driver):
        self.driver = driver

    def retail_login(self,uname, pwd):
        functions = Functions(self.driver)
        ele = functions.findEle(login_btn[0],login_btn[1])
        functions.hoverOverElement(ele)
        retail = functions.findEle(retail_link[0],retail_link[1])
        functions.clickEle(retail)
        functions.switchToTab(1)
        functions.enterTextElement(username_input[0],username_input[1],uname)
        functions.enterTextElement(password_input[0],password_input[1],pwd)
        functions.clickElement(retail_login_btn[0],retail_login_btn[1])



