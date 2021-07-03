import pytest
import yaml


def pytest_collection_modifyitems(session, config, items):
    # 遍历测试用例
    for item in items:
        # 重新编码测试用例名称
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 重新编码测试用例路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        #只要测试用例里有"login"出现，就给该测试用例加个标签，当只想执行测试用例中有”login“的用例，就用命令 pytest -m login即可
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)

def pytest_addoption(parser) :
    # 命令行中的参数都是分组的，比如general，collection，logging等，在每个组下都有一些具体的独立的参数
    mygroup = parser.getgroup("hogwarts")  # 添加一个组hogwarts，会将下面所有的option都展示在这个group下
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default = 'test', # 参数的默认值
                      dest = 'env',  # 存储的变量
                      help = 'set your run env')  # 帮助提示，参数的描述信息

# 通过fixture传递命令行参数
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env", default='test')
    if env == 'test':
        print("测试环境")
        datapath = 'datas/test/test.yaml'
    elif env == 'dev':
        print("开发环境")
        datapath = 'datas/dev/dev.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return env,datas



