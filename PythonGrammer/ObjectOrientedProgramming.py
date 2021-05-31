# 如果需要用类来访问方法，需要在方法前加个装饰器： @classmethod
# 类变量和实例变量
# 类方法和实例方法

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print(response.read())