import requests
import json
from tempfile import NamedTemporaryFile
import scripts.demo
import os

f = None


def login(captcha_id='', captcha_token=''):
    """
    登录接口，登录成功后回去用户的uid和token值
    """
    account = input('输入用户名:')
    password = input('输入密码:')
    header = {"platform": "ios"}
    payload = {
        "account": account,
        "password": password,
        "captcha_id": captcha_id,
        "captcha_token": captcha_token
    }
    r = requests.post("https://api.tuchong.com/accounts/login", data=payload, headers=header)
    result_content = r.json()
    print(result_content)

    result = result_content.get("result")
    code = result_content.get('code')

    if result == "ERROR" and code == 11:
        print('需要填写验证码')
        get_captcha()
    else:
        print('登录成功')
        token = result_content.get('token')
        uid = result_content.get('identity')
        save_token_uid(token, uid)


def get_captcha():
    """
    获取验证码后重新调用login接口进行登录
    :return: 验证码字符串
    """
    r = requests.post('https://api.tuchong.com/captcha/image')
    captcha_content = r.json()
    print(captcha_content)
    result = captcha_content.get('result')
    if result == 'SUCCESS':
        captcha_id = captcha_content.get('captchaId')
        captcha_base64 = captcha_content.get('captchaBase64')
        captcha_base64 = captcha_base64[21:len(captcha_base64)]
        words = oc_captcha(captcha_base64)
        login(captcha_id, words)
    else:
        return


def oc_captcha(img):
    """
    识别base64字符串中的数字验证码
    :param img: base64 图片字符串
    :return: 验证码
    """
    access_token = get_access_token()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    # f = open('[本地文件]', 'rb')
    # img = base64.b64encode(f.read())
    image_base64 = img
    params = {"image": image_base64}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        words_result = response.json().get('words_result')
        print(words_result)
        if len(words_result) == 0:
            oc_captcha(image_base64)
            return
        words = words_result[0].get('words')
        print(words)
        if len(words) != 4:
            oc_captcha(image_base64)
        return words


def get_access_token():
    """
    访问百度AI智能识别
    :return: access_token
    """
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           '&client_id=psumpBVxF36xPq9Y1cLGkvmG' \
           '&client_secret=CyxgStLBvE3hE2dF6WXLOjGKYnplEgDA'
    response = requests.get(host)
    if response:
        print(response.json())
        return response.json().get('access_token')


def save_token_uid(token, uid):
    save_file_path = './temp'
    if not os.path.isdir(save_file_path):
        os.makedirs(save_file_path)
    list_dir = os.listdir(save_file_path)
    if len(list_dir) != 0:
        for dir_temp in list_dir:
            os.remove(save_file_path + '/' + dir_temp)
    global f
    f = NamedTemporaryFile(mode='w+', dir=f'{save_file_path}/', delete=False)
    f.write(token+'\n')
    f.write(uid)
    f.seek(0)

