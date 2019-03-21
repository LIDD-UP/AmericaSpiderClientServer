# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: te_forevoer.py
@time: 2019/3/21
"""
from gevent import monkey
monkey.patch_all()
from flask import Flask
from gevent import wsgi

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello World'

server = wsgi.WSGIServer(('127.0.0.1', 5000), app)
server.serve_forever()