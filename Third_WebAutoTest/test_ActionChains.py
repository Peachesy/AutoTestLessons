from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        ele_double_click = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        ele_right_click = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_right_click)
        action.double_click(ele_double_click)
        sleep(3)
        action.perform()
        sleep(2)

    @pytest.mark.skip
    def test_move_to_ele(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//div[@class="s-top-right s-isindex-wrap"]/span[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele,drop_ele)
        # drag_and_drop使用了两个方法，action.click_and_hold(drag_ele).release(drop_ele).perform()
        # 同样效果的实现方法:
        # action.click_and_hold(drag_ele).move_to_element(drop_ele).release(.perform())
        sleep(2)
        action.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("Tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main(['test_ActionChains.py', '-vs'])
