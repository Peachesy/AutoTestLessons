import selenium
from selenium import webdriver
from time import sleep
import pytest


class TestAlert:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()


    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.switch_to.frame("iframeResult")

        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)

        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
