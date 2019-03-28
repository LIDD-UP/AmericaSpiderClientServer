#!/bin/bash

project1='zillow_main.py'


for Pro in $project1

do

PythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l `

echo $Pro
if [ $PythonPid -eq 0 ];
        then
        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is not running" >> /usr/project/logs/python.log

        cd /usr/project/EstateZillowSpider/AmericanRealEstate/
        
        nohup python3 $Pro > nohup.out 2>&1 &

#        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is starting" >> /usr/project/logs/python.log
        sleep 5
        CurrentPythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l`
        if [ $CurrentPythonPid -ne 0 ];
        then
        echo "`date "+%Y-%m-%d %H:%M:%S"`:$Pro is running" >> /usr/project/logs/python.log
        fi
fi
done
