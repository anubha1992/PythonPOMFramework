from selenium.webdriver import ActionChains

class Functions:
    def __init__(self,driver):
        self.driver = driver

    def findEle(self,locator, by):
        ele = self.driver.find_element(by,locator)
        return ele

    def clickEle(self,ele):
        ele.click()

    def clickElement(self,locator, by):
        ele = self.driver.find_element(by,locator)
        ele.click()

    def hoverOverElement(self,ele):
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()

    def enterText(self,ele,txt):
        ele.send_keys(txt)

    def enterTextElement(self,locator, by,txt):
        ele = self.driver.find_element(by,locator)
        ele.send_keys(txt)

    def isElementDisplayed(self,locator,by):
        displayed = len(self.driver.find_elements(by,locator)) > 0
        return displayed

    def switchToTab(self,tabNum):
        handle1 =  self.driver.window_handles[tabNum]
        self.driver.switch_to.window(handle1)

    def switchToMainWindow(self):
        self.driver.switch_to.default_content()







