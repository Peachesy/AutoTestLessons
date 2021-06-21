import pytest


@pytest.mark.parametrize('name',['赫敏','哈利','露娜'])
def test_name(name):
    print(name)
