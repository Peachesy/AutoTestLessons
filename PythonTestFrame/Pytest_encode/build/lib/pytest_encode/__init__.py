from typing import List

import pytest


def pytest_collection_modifyitems(session, config, items:List):
    # 遍历测试用例
    for item in items:
        # 重新编码测试用例名称
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 重新编码测试用例路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        #只要测试用例里有"login"出现，就给该测试用例加个标签，当只想执行测试用例中有”login“的用例，就用命令 pytest -m login即可
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)