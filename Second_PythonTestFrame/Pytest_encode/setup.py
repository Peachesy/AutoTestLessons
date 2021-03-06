from setuptools import setup

setup(
    name = 'pytest_encode',
    url = 'https://github.com/XXX/pytest_encode',
    version = '1.0',
    author = 'peachesy',
    author_email = '2360950972@qq.com',
    description = 'set your encoding and logger',
    long_description = 'Show Chinese for your mark.parametrize(). Define logger variable',
    classifiers = [ # 分类索引
        'Framework::Pytest',
        'Programming Language::Python',
        'Topic::Software Development::Testing',
        'Programming Language::Python::3.8',
    ],
    license = 'proprietary',
    packages = ['pytest_encode'],
    keywords = ['pytest','py.test','pytest_encode'],

    #需要安装的依赖
    install_requires = ['pytest'],

    # 入口模块或者入口函数,pytest11是一个固定用法！
    entry_points={
        'pytest11':[
            'pytest_encode = pytest_encode'
        ]
    },

    zip_safe = False
)