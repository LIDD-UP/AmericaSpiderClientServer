#!/bin/bash
tmp=`ps -ef | grep "/usr/bin/python3 runserver.py"| grep -v grep | awk '{print $2}'`
# tmp=`ps -ef | grep "/usr/bin/python3 /data/project/AmericaSpiderClientServer/runserver.py"| grep -v grep | awk '{print $2}'`
echo ${tmp}
kill -9 ${tmp}
