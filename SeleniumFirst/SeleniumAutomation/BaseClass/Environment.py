from selenium import webdriver

class Environment():

    def setUp(self):
        self.driver = webdriver.Chrome("..\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.starhealth.in/")
        self.driver.set_script_timeout(10)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        self.driver.quit()


