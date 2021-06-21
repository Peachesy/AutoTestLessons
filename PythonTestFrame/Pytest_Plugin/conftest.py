
def pytest_collection_modifyitems(session, config, items):
    # 遍历测试用例
    for item in items:
        # 重新编码测试用例名称
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # 重新编码测试用例路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')