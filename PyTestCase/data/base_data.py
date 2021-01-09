import os
import scripts.login_for_name


def get_token_uid():
    file_path = './temp'
    if os.path.exists(file_path):
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
        print(token + '...' + uid)
        user_dict = {
            'token': token,
            'uid': uid
        }
    return user_dict
