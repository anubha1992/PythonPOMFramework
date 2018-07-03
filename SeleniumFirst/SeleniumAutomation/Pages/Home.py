from selenium import webdriver
from SeleniumAutomation.Utilities.Functions import Functions
from selenium.webdriver.common.by import By
from SeleniumAutomation.Pages.Home_Locator import *


class Login(object):

    def __init__(self,driver):
        self.driver = driver

    # def login(self,uname,pwd):
    #     functions = Functions(self.driver)
    #     ele = functions.findEle(self.driver)
    #     functions.hoverOverElement(ele)


    def verify_Login_success(self):
        functions = Functions(self.driver)
        assert functions.isElementDisplayed(logout_link[0],logout_link[1]) == True










