from selenium import webdriver
import pytest

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  #隐式等待

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-29703 .title > a").click()

# # python文件的入口函数
# if __name__=="__main__":
#         pytest.main()
