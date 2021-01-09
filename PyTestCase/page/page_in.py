from tool.get_driver import GetDriver
from page.page_login import PageLogin


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()
        try:
            self.driver.find_elements_by_id('xxx:id/permission_allow_xxx').click()
        except:
            pass

    def page_get_pagelogin(self):
        return PageLogin(self.driver)
