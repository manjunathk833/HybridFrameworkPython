import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("******************** Test_001_Homepage ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.logger.info("******************** Test_001_Verifying title ****************")

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************** Test_001_Home Page Title Test Passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePAgeTitle.png")
            self.driver.close()
            self.logger.info("******************** Test_002_Home page test is failed ****************")
            assert False

    def test_login(self, setup):
        self.logger.info("******************** Test_002_Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.logger.info("******************** Test_002_Verifying Title after login ****************")
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.error("******************** Test_002_Login Test Passed****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******************** Test_002_Login Test Failed ****************")
            assert False