# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: settings.py
@time: 2019/3/15
"""
import pandas as pd

# local configure
# spider_root_path = r'F:\PycharmProject\AmericanRealEstate'
# spider_root_path = r'G:\PycharmProject\AmericanRealEstate'
# detial_spider_main_path = spider_root_path + r'\realtor_a_main.py'
# list_spider_main_path = spider_root_path + r'\realtor_list_page_main.py'

# server configure
spider_root_path = r'/data/project/AmericanRealEstate'
detial_spider_main_path = spider_root_path + r'/realtor_a_main.py'
list_spider_main_path = spider_root_path + r'/realtor_list_page_main.py'


detail_search_criteria_save_path = spider_root_path + '/crawl_tools'

spider_client_server_root_path = '/data/project/AmericaSpiderClientServer'
close_client_server_shell_path = spider_client_server_root_path + '/close_realtor_client_server.sh'











