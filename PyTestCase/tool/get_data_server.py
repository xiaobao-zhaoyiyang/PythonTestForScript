import requests
import json

from tool import get_data_excel


def get_data(url):
    headers = {
        'method': 'GET',
        'authority': 'tuchong.com',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'webp_enabled=1',
        'cookie': 'token=5180c542c8307b54',
        'cookie': 'lang=zh',
        'cookie': 'PHPSESSID=inejn5iuengq7muiqos0eeuaef',
        'cookie': '_ga=GA1.2.1056662492.1606553476',
        'cookie': '_gid=GA1.2.304345705.1606553476',
        'cookie': 'MONITOR_WEB_ID=49b75dbd-30e5-49b8-b40f-1fc031cb4a7a',
        'cookie': '_gat=1'
    }
    r = requests.get(url, headers)
    # print(r.status_code)
    data = r.json()
    # print(json.dumps(data))
    return data


def get_compair_data(filepath, index):
    #打开本地文件
    table = get_data_excel.excel.open_excel(filepath, index)
    #获取title
    title = get_data_excel.excel.read_title_from_excel(table)
    # print('title = %s'%title)
    # 获取本地数据
    tables = get_data_excel.excel.read_excel(table, title)

    for num in range(table.nrows-1):
        #获取本地数据
        array_excel = tables[num]
        # print('本地数据%s'%array_excel)
        #获取课程id
        id = int(array_excel['id'])
        t = type(id)
        # print('课程id=%s, id的类型%s'%(id, t))
        #根据id获取网络数据
        data = get_data('https://tuchong.com/gapi/misc/paid-course/course-group/detail?course_group_id=%s'%id)
        # if data.re
        result = data['result']
        if result == 'ERROR':
            print('请求失败：message = %s' % data['message'])
            break
        course_group = data['course_group']
        # 根据title获取实际需要数据
        array_url = {}
        for cnum in range(table.ncols):
            value = title[cnum]
            # print('value=%s,是否为空 %s' % (value, value.isspace()))
            if len(value) == 0:
                array_url[value] = ''
                continue
            if value == 'name' or value == 'site_id':
                site = course_group['site']
                array_url[value] = site[value]
            elif value == 'tag_id' or value == 'tag_name':
                tags = course_group['tags']
                tag = tags[0]
                array_url[value] = tag[value]
            elif value == 'price' or value == 'original_price':
                array_url[value] = course_group[value]/100
            elif value == 'course_count':
                array_url[value] = str(course_group[value])
            else:
                value_url = course_group[value]
                array_url[value] = value_url
        # print('网络数据%s'%array_url)
        #比较数据出结果
        if array_excel == array_url:
            print('课程id = %s，True' % id)
        else:
            print('课程id = %s，False' % id)
            #读取两个字典相同的key
            diff = array_excel.keys() & array_url
            #key相同但value不同
            diff_vals = [(k, array_excel[k], array_url[k]) for k in diff if array_excel[k] != array_url[k]]
            print('本地数据%s' % array_excel)
            print('网络数据%s' % array_url)
            print(diff_vals)


if __name__ == '__main__':
    # get_data()
    get_compair_data('/Users/zhaoqiang/Documents/MyFiles/上架课程.xlsx', 1)