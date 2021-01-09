import scripts.login_for_name
import requests

headers = {}


def get_data_from_url():
    scripts.login_for_name.login()
    print('token = ' + scripts.login_for_name.token)
    url = f'https://api.tuchong.com/sites/{scripts.login_for_name.uid}/works'
    global headers
    headers = {'token': scripts.login_for_name.token,
               'platform': 'ios'}
    r = requests.get(url, headers=headers)
    print(r.json())
    return r.json()


def analysis_json():
    list_simple_json = []
    result_content = get_data_from_url()
    count = result_content.get('count')
    if count > 0:
        work_list = result_content.get('work_list')
        for single_data in work_list:
            data_type = single_data.get('type')
            entry = single_data.get('entry')
            if 'new_film' == data_type or 'video' == data_type:
                data_id = entry.get('vid')
                is_self = entry.get('is_self')
            elif 'post' == data_type:
                data_id = entry.get('post_id')
            is_top = entry.get('is_top')
            dict_simple_data = {
                'id': data_id,
                'type': data_type,
                'is_self': is_self,
                'is_top': is_top
            }
            list_simple_json.append(dict_simple_data)
    print(list_simple_json)
    return list_simple_json


def delete_single_data(single_data):
    # list_simple_json = analysis_json()
    # single_data = list_simple_json[index]
    data_type = single_data.get('type')
    data_id = single_data.get('id')
    is_top = single_data.get('is_top')
    url_post = f'https://api.tuchong.com/posts/{data_id}'
    url_else = f'https://api.tuchong.com/video/{data_id}'
    if is_top:
        print('置顶作品，建议留存')
        return
    if 'new_film' == data_type or 'video' == data_type:
        r = requests.delete(url_else, headers=headers)
        print('删除了视频类：' + r.json())
    else:
        r = requests.delete(url_post, heeaders=headers)
        print(r.json())
        print('删除了图文类：' + r.json())


def delete_all_data(is_delete_all):
    list_simple_json = analysis_json()
    for single_data in list_simple_json:
        if not is_delete_all:
            delete_single_data(single_data)
            return


if __name__ == '__main__':
    delete_all_data(False)