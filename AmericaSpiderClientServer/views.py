from AmericaSpiderClientServer import app
from flask import request, redirect
import json
import os
import sys
import requests
import time
import threading

from AmericaSpiderClientServer.settings import detial_spider_main_path, spider_root_path,list_spider_main_path


# 开启列表页爬虫
@app.route('/start_list_spider/', methods={"POST","GET"})
def start_list_spider():
    # data = request.get_data()
    # print(data)
    print("执行list爬虫")
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python {}".format(list_spider_main_path))
    return "execute successfully"


# 详情页爬虫启动
@app.route('/start_detail_spider/',methods={"POST","GET"})
def start_detail_spider():
    data = request.get_data()
    print(data)
    print("执行详情页爬虫")
    import os
    import sys
    detial_path = detial_spider_main_path
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python {}".format(detial_path))
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


