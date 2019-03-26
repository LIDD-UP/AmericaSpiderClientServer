# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: redis_scard_test.py
@time: 2019/3/26
"""
import redis
pool = redis.ConnectionPool(
                # host='106.12.196.86',
                # host='127.0.0.1',
                # host = '138.197.143.39',
                host='106.12.196.106',
                # host='39.106.17.15',
                # password='123456'
            )
redis_pool = redis.Redis(connection_pool=pool)

# redis_pipeline = redis_pool.pipeline()
# count = redis_pipeline.scard('realtor:list_url')
# print(count)
# redis_pipeline.execute()
count = redis_pool.llen("realtor:list_url")

print(count)