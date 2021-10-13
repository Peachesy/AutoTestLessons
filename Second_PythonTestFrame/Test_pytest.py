import pytest
import yaml


class TestDemo:
    # !!!测试类不能有__init__方法!!!

    @pytest.fixture()
    def login(self):
        print("执行测试用例前需要先登录哦~")
        username = "Jerry"
        return username

    def test_a(self,login):  # 调用lgoin方法
        print(f"I am test_a and my name is {login}.")

    def test_b(self):
        print("I am test_b and do nothing.")



def func(x):
    return x+1

@pytest.mark.parametrize('a,b',yaml.safe_load(open('./data.yaml')))  # 列表中的数据是执行该测试用例时的测试数据
def test_answer(a,b):
    assert func(a)==b

# python文件的入口函数
if __name__ == '__main__':
    pytest.main(['Test_pytest.py::test_answer','-v'])