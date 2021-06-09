import time
import allure
import pytest
from selenium import webdriver


@allure.feature("百度搜索")  # 测试的功能：百度搜索
@allure.description("""测试百度搜索的纯文本搜索和域名搜索功能""")
class Test_Allure:

    url = "https://www.baidu.com/"
    driver = webdriver.Chrome("D:\Applications\WebDrivers")
    driver.get(url)

    # def OpenBrowsers(self):


    @allure.story("纯文本搜索")
    @allure.link("https://www.baidu.com/", name="百度首页")
    @allure.description("""该方法主要是在百度搜索中搜索一个关键词并对结果截屏保存，最后生成测试报告""")  # 添加测试描述
    @pytest.mark.parametrize('keywords',['allure','pytest','selenium'])  # pytest参数化用例
    def test_search_text(self,keywords):
        with allure.step("打开百度首页"):  # step方法和with一起使用，方便区分不同的step
            driver = webdriver.Chrome("D:\Applications\WebDrivers")
            url = "https://www.baidu.com/"
            driver.get(url)

        with allure.step(f"搜索关键词:{keywords}"):  # 在纯文本描述中引入变量
            driver.find_element_by_id("kw").send_keys(keywords)
            time.sleep(2)
            driver.find_element_by_id("su").click()
            time.sleep(2)

        with allure.step("保存截图"):
            driver.save_screenshot("./Result/sreenshot.png")
            # 把截图放到测试报告中
            allure.attach.file('./Result/screenshot.png',attachment_type=allure.attachment_type.PNG)
            # 把部分HTML放到测试报告中
            allure.attach('<head></head><body>首页</body>','Attach with HTML type',attachment_type=allure.attachment_type.HTML)

        with allure.step("关闭浏览器"):
            driver.quit()

    @allure.story("域名搜索")
    @allure.link("https://www.baidu.com/",name="百度首页")
    @allure.description("""该方法主要是在百度搜索中搜索一个域名并对结果截屏保存，最后生成测试报告""")  # 添加测试描述
    @pytest.mark.parametrize('keywords', ['site:csdn.net'])  # pytest参数化用例
    def test_search_domain(self,keywords):
        with allure.step("打开百度首页"):  # step方法和with一起使用，方便区分不同的step
            driver = webdriver.Chrome("D:\Applications\WebDrivers")
            url = "https://www.baidu.com/"
            driver.get(url)

        with allure.step(f"搜索关键词:{keywords}"):  # 在纯文本描述中引入变量
            driver.find_element_by_id("kw").send_keys(keywords)
            time.sleep(2)
            driver.find_element_by_id("su").click()
            time.sleep(2)

        with allure.step("保存截图"):
            driver.save_screenshot("./Result/sreenshot.png")
            # 把截图放到测试报告中
            allure.attach.file('./Result/screenshot.png', attachment_type=allure.attachment_type.PNG)
            # 把部分HTML放到测试报告中
            allure.attach('<head></head><body>首页</body>', 'Attach with HTML type',
                          attachment_type=allure.attachment_type.HTML)

        with allure.step("关闭浏览器"):
            driver.quit()

