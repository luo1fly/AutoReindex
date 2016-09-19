#!/usr/bin/env python
# Name: main.py
# Time:9/19/16 2:08 PM
# Author:luo1fly

from utils.mysql_helper import MysqlHandler
from utils.process_helper import ProcessHandler
from logging.config import fileConfig
import logging
from conf import settings
import time
import sys
# import custom modules above


class Main(object):
    """

    """
    def __init__(self):
        fileConfig('conf/logger.conf')
        self.error_logger = logging.getLogger('errorLogger')
        self.info_logger = logging.getLogger('infoLogger')

    def run(self):
        """
        1.select remote last modify time
        2.if less than 24h nothing to do else rebuild index
        3.subprocess
        :return:
        """
        mh = MysqlHandler(self)
        last = mh.select(settings.LAST)
        last_modify = last.timestamp()
        date_diff = (time.time() - last_modify) / 3600
        if date_diff < settings.INTERVAL:
            self.info_logger.info('检查完成同步正常')
            sys.exit(0)
        else:
            mh.truncate(settings.TRUNCATE)
            mh.close()
            self.info_logger.info('UpdateIndex has been truncated...')
            ph = ProcessHandler()
            pid = ph.get_pid()
            if not pid:
                ph.start_index()
                self.info_logger.info('just started index build process')
            else:
                ph.stop_index()
                flag = ph.get_pid()
                count = 100
                while not flag:
                    ph.start_index()
                    flag = ph.get_pid()
                    count -= 1
                    if count <= 0:
                        self.error_logger.error('something was wrong whith index build script,please check!!!')
                        sys.exit(1)
                self.info_logger.info('index build process has been restart')




