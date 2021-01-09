from selenium.webdriver.support.wait import WebDriverWait
from tool import get_driver

class Base:
    # def __init__(self, driver):
    #     self.driver = driver

    driver = None
    def __init__(self):
        driver = get_driver.GetDriver.get_driver()

    # 查找元素
    def base_find(*loc, timeout=10, poll=0.5):
        return WebDriverWait(Base.driver, timeout=timeout, poll_frequency=poll).until(lambda driver: (Base.driver).find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        # 获取
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 点击方法
    def base_click(self, *loc):
        self.base_find(*loc).click()
