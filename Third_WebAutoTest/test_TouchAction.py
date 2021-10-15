from selenium import webdriver
from selenium.webdriver import TouchActions
import pytest
from time import sleep

class TestTouchAction():
    def setup(self):
        # 有报错：unknown command: Cannot call non W3C standard.解决：在打开chrome前添加一个参数
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)

        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        ele_input = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele_input.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele_search,0,10000).perform()
        sleep(3)



if __name__ == '__main__':
    pytest.main(['test_TouchAction.py', '-vs'])