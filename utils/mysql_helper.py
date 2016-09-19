#!/usr/bin/env python
# Name: mysql_helper.py
# Time:9/19/16 2:42 PM
# Author:luo1fly

import pymysql
import sys
import datetime
from conf import settings
# import custom modules above


class MysqlHandler(object):

    def __init__(self, main_ins):
        self.error_logger = main_ins.error_logger
        # self.info_logger = main_ins.info_logger
        conn_dic = settings.CONN_MYSQL
        self.__conn = self.__login(conn_dic)

    def __login(self, conn_dic):
        try:
            conn = pymysql.connect(**conn_dic)
        except pymysql.OperationalError as e:
            self.error_logger.error('%s' % e.args[0])
            sys.exit(1)
        else:
            return conn

    def select(self, cmd):
        cur = self.__conn.cursor()
        cur.execute(cmd)
        result = cur.fetchone()
        cur.close()
        if not result:
            return datetime.datetime(1990, 1, 1, 0, 0)
        else:
            return result[1]

    def truncate(self, cmd):
        cur = self.__conn.cursor()
        cur.execute(cmd)
        self.__conn.commit()
        cur.close()

    def close(self):
        self.__conn.close()
