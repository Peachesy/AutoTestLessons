import pytest
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import expected_conditions

class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
        self.driver.get("https://ceshiren.com/")
        # 隐式等待
        # self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()


    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        # # 直接等待
        # time.sleep(3)

        # 为显式等待设置条件
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) > 1

        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@title="有新帖子的话题"]')))
        self.driver.find_element(By.XPATH, '//*[@title="有新帖子的话题"]').click()

        # print("Hello, I have wait for 3 second~")
#
# if __name__=="__main__":
#         pytest.main(['test_wait.py','-v'])