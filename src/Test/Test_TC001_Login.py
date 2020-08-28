import unittest
from selenium import webdriver
from time import sleep
from Utility.ExcelReader import getData
from src.BaseClass import EnvironmentSetup
from src.Utility import ExcelReader

class TC001_login(EnvironmentSetup):

    def test_login(self):
        self.driver.get("http://seamlessly.net")
        path = ("DataDrivenTesting\src\TestData\TestData.xlsx")
        data = getData(path, "userData")

        for i in data:
            # fetching data from excel and storing it to variable:
            print("Logged in with : "+str(data['username'][i])+ '/' +  str(data['password'][i]))


if __name__ == '__main__':
    unittest.main()