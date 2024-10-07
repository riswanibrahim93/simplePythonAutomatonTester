"""
    This module place for keyword
"""
from exceptiongroup import catch
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Keyword:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, strUrl):
        self.driver.get(strUrl)

    def click(self, strXpath):
        try:
            webEle = self.driver.find_element(By.XPATH,strXpath)
            webEle.click()
        except:
            self.driver.execute_script("arguments[0].click();", webEle)

    def set_text(self, strXpath, strValue):
        webEle = self.driver.find_element(By.XPATH,strXpath)
        webEle.send_keys(strValue)

    def get_text(self, strXpath):
        webEle = self.driver.find_element(By.XPATH,strXpath)
        strText = webEle.text
        return strText

    def get_all_text(self, strXpath):
        listTexts = self.driver.find_elements(By.XPATH,strXpath)
        titles = [strText.text for strText in listTexts]
        return titles

    def scroll_into_view(self, strXpath):
        webEle = self.driver.find_element(By.XPATH, strXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", webEle)

    def move_to_element(self, strXpath):
        webEle = self.driver.find_element(By.XPATH, strXpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(webEle).perform()