from AmericaSpiderClientServer import app
from flask import request, redirect
import json
import os
import sys
import requests

from AmericaSpiderClientServer.settings import detial_spider_main_path, spider_root_path,list_spider_main_path


# 开启列表页爬虫
@app.route('/start_list_spider/', methods={"POST","GET"})
def start_list_spider():
    # data = request.get_data()
    # print(data)
    print("执行list爬虫")
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python3 {}".format(list_spider_main_path))
    return "execute successfully"


# 详情页爬虫启动
@app.route('/start_detail_spider/',methods={"POST","GET"})
def start_detail_spider():
    data = request.get_data()
    print(data)
    print("执行爬虫")
    import os
    import sys
    detial_path = detial_spider_main_path
    sys.path.append(spider_root_path)
    os.chdir(spider_root_path)
    os.system(r"python3 {}".format(detial_path))
    return "execute successfully"
