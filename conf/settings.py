#!/usr/bin/env python
# Name: settings.py.py
# Time:9/19/16 1:57 PM
# Author:luo1fly


# import custom modules above


# define your variables below

# ssh credentials of remote server
CONN_SSH = dict(
    IP='58.222.17.201',
    port=22,
    username='root',
    password=''
)

# mysql connection credentials
CONN_MYSQL = dict(
    db='Search',
    host='58.222.17.196',
    passwd='',
    port=3306,
    user='root'
)

# sql queries
LAST = 'SELECT * FROM UpdateIndex;'
TRUNCATE = 'TRUNCATE TABLE UpdateIndex;'

# 允许最大时间差
INTERVAL = 24

# 获取MicSeIndex进程pid命令
PID = "ps aux|grep MicSeIndex|grep -v grep|awk '{print $2}'"
START_INDEX = '/usr/local/micse/startIndex'
