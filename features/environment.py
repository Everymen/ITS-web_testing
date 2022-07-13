from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from behave import *


def get_driver():
        """Get Chrome/Firefox driver from Selenium Hub"""
        try:
            driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.FIREFOX)
        except:
            driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.implicitly_wait(5)
        return driver

def before_all(context):
        #context.browser = webdriver.Firefox()
        context.driver = get_driver()
        context.base_url = "http://localhost:8080/VALU3S"

def after_all(context):
  
        context.driver.close()
        context.driver.quit()
        pass

def after_scenario(context, scenario):
    context.driver.get("http://localhost:8080/VALU3S/logout")
#    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
#    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
#    context.driver.find_element(By.ID, "personaltools-logout").click()
    pass    
