# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: te_class.py
@time: 2019/3/26
"""
import time
realtor_list_search_criteria = [0,1,2,3,4]

class GetListSearchCriteria(object):
    offset = 0
    realtor_list_search_criteria_len = len(realtor_list_search_criteria)
    batch_size = 200
    get_time = 0
    total_get_time = int(realtor_list_search_criteria_len/batch_size)
    division = realtor_list_search_criteria_len % batch_size
    is_exact_division = True if division == 0 else False

    def __init__(self):
        pass

    def get_list_url(self):
        present_time = self.get_time + 1
        if present_time <= self.total_get_time:
            start_index = self.offset
            end_index = start_index + self.batch_size -1
            self.offset += self.batch_size

        if present_time > self.total_get_time and self.is_exact_division is False:
            start_index = self.offset
            end_index = start_index + self.division
            GetListSearchCriteria.offset += end_index
            print('xx')

    @classmethod
    def te_class(cls):
        cls.offset +=5


if __name__ == '__main__':
    # # while True:
    # #     # time.sleep(5)
    # xx = GetListSearchCriteria()
    # xx.te_class()
    # # xx.get_list_url()
    #
    # print(xx.offset)
    # print(GetListSearchCriteria.offset)
    #
    # yy = GetListSearchCriteria()
    # # yy.get_list_url()
    # yy.te_class()
    # print(xx.offset)
    # print(GetListSearchCriteria.offset)
    while True:
        GetListSearchCriteria.offset +=1
        print(GetListSearchCriteria.offset)
        time.sleep(5)