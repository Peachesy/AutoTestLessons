import pytest


@pytest.mark.parametrize('name',['赫敏','哈利','露娜'])
def test_name(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login")
    assert False

def test_search():
    print("search")

def test_env(cmdoption):
    # print(cmdoption)
    env,datas = cmdoption  # 接收env和datas数据
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host)+":"+str(port)
    print(url)