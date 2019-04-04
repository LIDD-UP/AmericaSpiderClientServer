from AmericaSpiderClientServer import app
from flask import request, redirect
import json
import os
import sys
import requests
import time
import threading
import pandas as pd

from AmericaSpiderClientServer.settings import detial_spider_main_path, spider_root_path,list_spider_main_path
from AmericaSpiderClientServer.settings import detail_search_criteria_save_path
from AmericaSpiderClientServer.settings import close_client_server_shell_path


# 开启列表页爬虫
@app.route('/start_list_spider/', methods={"POST","GET"})
def start_list_spider():
    # data = request.get_data()
    # print(data)
    print("执行list爬虫")
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python3 {}".format(list_spider_main_path))
    # os.system(r"python {}".format(list_spider_main_path))
    return "execute successfully"


# 详情页爬虫启动
@app.route('/start_detail_spider/',methods={"POST","GET"})
def start_detail_spider():
    data = request.get_data()
    print("执行详情页爬虫")
    import os
    import sys
    detial_path = detial_spider_main_path
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python3 {}".format(detial_path))
    # os.system(r"python {}".format(detial_path))
    return "execute successfully"


def test_threading(url):
    print("沉睡5秒开始")
    time.sleep(5)
    req = requests.get(url=url)
    print(req.text)
    print("沉睡5秒结束")


@app.route('/test/',methods={"POST","GET"})
def test():
    thread1 = threading.Thread(target=test_threading, args=('www.baidu.com',))
    thread1.start()
    thread2 = threading.Thread(target=test_threading, args=('www.baidu.com',))
    thread2.start()
    thread3 = threading.Thread(target=test_threading, args=('www.baidu.com',))
    thread3.start()
    return "process success!"


@app.route('/get_detail_search_criteria/',methods={"POST","GET"})
def get_detail_search_criteria():
    json_data = request.get_json()
    print("detail 爬虫接受爬取条件数据成功")
    dict_data = json.loads(json_data)
    property_id_list = dict_data['data']
    property_id_list = ['https://mapi-ng.rdc.moveaws.com/api/v1/properties/{}?client_id=rdc_mobile_native%2C9.3.7%2Candroid'.format(property_id) for property_id in property_id_list]

    property_id_df = pd.DataFrame(property_id_list, columns=['detail_criteria'])

    property_id_df.to_csv(detail_search_criteria_save_path + '/realtor_app_detail_page_search_criteria.csv', index=False)

    print('detail 爬虫数据存储到本地csv文件完成，准备开启detail爬虫')
    return redirect('/start_detail_spider/')


@app.route('/test_compress_data_post/',methods={"POST","GET"})
def test_compress_data_post():
    # data = request.get_json()
    data = request.get_data()
    print(len(data))
    return 'yes'


@app.route('/close_client_server/',methods={"POST","GET"})
def close_client_server():
    os.system('/bin/sh {}'.format(close_client_server_shell_path))
    return 'yes'






