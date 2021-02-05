import os
import scripts.login_for_name


def get_token_uid():
    file_path = '/Users/zhaoqiang/pycharm-workspace/PyTestCase/data/temp'
    # print(file_path)
    if not os.path.exists(file_path):  # 文件夹不存在，直接调用登录
        scripts.login_for_name.login()
    if os.path.exists(file_path):  # 文件夹存在
        # print('存在文件夹。。。。。。')
        file_list = os.listdir(file_path)
        if len(file_list) == 0:
            scripts.login_for_name.login()
            file_list = os.listdir(file_path)
        for file_name in file_list:
            file_name = file_path + "/" + file_name
        file = open(file_name)
        token = file.readline()
        if token.endswith('\n'):
            token = token.strip('\n')
        uid = file.readline()
        # print(token + '...' + uid)
        user_dict = {
            'token': token,
            'uid': uid
        }
        file.close()
        return user_dict
