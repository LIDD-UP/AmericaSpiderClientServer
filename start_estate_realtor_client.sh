#!/bin/bash

project1='runserver.py'


for Pro in $project1

do

PythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l `

echo $Pro
if [ $PythonPid -eq 0 ];
        then
        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is not running" >> /data/project/AmericaSpiderClientServer/realtor_client.log

        cd /data/project/AmericaSpiderClientServer/
        
        nohup python3 $Pro > nohup.out 2>&1 &

        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is starting" >> /data/project/AmericaSpiderClientServer/realtor_client.log
        sleep 5
        CurrentPythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l`
        if [ $CurrentPythonPid -ne 0 ];
        then
        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is running" >> /data/project/AmericaSpiderClientServer/realtor_client.log
        fi
fi
done
