from selenium import webdriver


class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test(self):
        print("我是Base类的test方法")