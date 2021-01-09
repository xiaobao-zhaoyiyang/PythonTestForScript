from tool.read_yaml import read_yaml
import page.page_login
import page.page_in


def get_data():
    user = {'username': '', 'password': 0}
    for data in read_yaml('login.yaml').values():
        user['username'] = data['username']
        user['password'] = data['password']
        # print('startLogin, username = ' + user['username'] + 'pwd = ' + user['pwd'])
        return user


class TestLogin:
    print('startTest.......')

    def setup_class(self):
        print('setup_class')
        page.page_in.PageIn
        pass

    def teardown_class(self):
        print('teardown_class')
        pass

    def test_login(self):
        # print('startLogin, username = ' + get_data()['username'] + 'pwd = ' + get_data()['pwd'])
        login = page.page_login.PageLogin
        login.page_login(login, get_data()['username'], get_data()['password'])
        # page.page_login.PageLogin.page_login(self, get_data()['username'], get_data()['password'])


if __name__ == '__main__':
    print(get_data())
    page.page_in.PageIn
