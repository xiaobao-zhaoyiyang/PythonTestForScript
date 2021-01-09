from base.base import Base
import page


class PageLogin(Base):
    def page_jump_login_name_pwd(self):
        Base.base_click(Base, page.login_name_pwd)

    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    def page_click_login(self):
        self.base_click(page.login_btu)

    def page_login(self, username, pwd):
        self.page_jump_login_name_pwd(self)
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login(self)
