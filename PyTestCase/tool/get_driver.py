from appium import webdriver
from selenium import webdriver
from tool.read_yaml import read_yaml


def get_tips_message():
    # 获取统一错误提示框信息
    msg = GetDriver.get_driver().find_element_by_class_name('xxx-layer-conntent').text
    print(f'msg={msg}')
    return msg


class GetDriver:
    driver = None  # 设置浏览器初始化状态

    # 获取driver对象
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            caps = {}
            for data in read_yaml('caps.yaml').values():
                caps['deviceName'] = data.get('deviceName')
                caps['appPackage'] = data.get('appPackage')
                caps['appActivity'] = data.get('appActivity')
                caps['platformName'] = data.get('platformName')
                caps['platformVersion'] = data.get('platformVersion')
                caps['autoGrantPermissions'] = data.get('autoGrantPermissions')
            # cls.driver = webdriver.Remote('http://127.0.0.1:44444', caps)
            # cls.driver.implicitly_wait(10)

            cls.driver = webdriver.chrome()
            cls.driver.get("http://www.baidu.com")

        return cls.driver
