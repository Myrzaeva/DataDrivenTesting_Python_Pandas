import unittest
from selenium import webdriver
from webdriver_manager import chrome
import datetime
class EnvironmentSetup(unittest.TestCase):

    #setup contains the browser setup attributes:
    @classmethod
    def setUP(self):
        self.driver = webdriver.Chrome()
        print("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("-------------------------------------------------")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    @classmethod
    def tearDown(self):
        if(self.driver != None):
            print("---------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
