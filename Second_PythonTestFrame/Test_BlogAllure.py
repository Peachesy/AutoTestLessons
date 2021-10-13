import pytest
import allure


@allure.title("title:功能层级的title")
@allure.feature("登录模块")
class TestLogin():

    @allure.title("title:登录成功测试用例")
    @allure.story("Story:登录成功")
    @allure.link("www.baidu.com",name="测试用例地址")
    @allure.description("这是一个测试用例描述")
    def test_login_success(self):
        print("登录成功测试用例")
        pass

    @allure.title("title:登录失败测试用例")
    @allure.story("Story:登录失败")
    @allure.description_html("""
    <h1>这是一个用HTML来描述的测试用例</h1>
    <table style="width:100%">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
      </tr>
      <tr align="center">
        <td>William</td>
        <td>Smith</td>
        <td>50</td>
      </tr>
      <tr align="center">
        <td>Vasya</td>
        <td>Jackson</td>
        <td>94</td>
      </tr>
    </table>
    """)
    def test_login_fail(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入错误的密码")
        with allure.step("点击登录"):
            print("点击登录")
        print("登录失败测试用例")

        # 把部分HTML放到测试报告附件中
        allure.attach('<head></head><body>登录失败</body>', 'Attach with HTML type',attachment_type=allure.attachment_type.HTML)
        pass

    @allure.title("title:登录时用户名缺失测试用例")
    @allure.story("Story:用户名缺失")
    def test_lossUserName(self):
        print("用户名缺失测试用例")
        pass

    @allure.title("title:登录时密码缺失测试用例")
    @allure.story("Story:密码缺失")
    def test_lossPassword(self):
        print("缺失密码测试用例")
        pass