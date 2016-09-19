#!/usr/bin/env python
# Name: ssh_helper.py
# Time:9/19/16 1:51 PM
# Author:luo1fly

import paramiko
import sys
from conf import settings
# import custom modules above


class SSHHandler(object):
    def __init__(self, main_ins):
        self.error_logger = main_ins.error_logger
        # self.info_logger = main_ins.info_logger
        conn_dic = settings.CONN_SSH
        self.__conn = self.__login(conn_dic)

    def __login(self, conn_dic):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(**conn_dic)
        except paramiko.AuthenticationException as e:
            self.error_logger.error('%s' % e.args[0])
            sys.exit(1)
        else:
            return ssh

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.__conn.exec_command(cmd)
        result = (stdout.read()+stderr.read()).decode('utf8')
        return result

    def close(self):
        self.__conn.close()
