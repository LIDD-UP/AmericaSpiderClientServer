# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: response_text_test.py
@time: 2019/3/26
"""
import requests

req = requests.get(url='http://127.0.0.1:8000/spider_server/get_list_search_criteria/')
print(req.text)
if req.text=='list页搜索条件已经空了':
    print('yes')