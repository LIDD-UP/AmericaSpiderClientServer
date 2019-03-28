# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: check_json.py
@time: 2019/3/28
"""
import requests
import json

req = requests.get(url='https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset=0&limit=200&county=Union&state_code=IL&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid')
req_dict =json.loads(req.text)
for i,value in enumerate(req_dict['listings']):
    print(i,value)
