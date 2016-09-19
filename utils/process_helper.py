#!/usr/bin/env python
# Name: process_helper.py
# Time:9/19/16 3:43 PM
# Author:luo1fly

import subprocess
from conf import settings
# import custom modules above


class ProcessHandler(object):
    """

    """
    def get_pid(self):
        ret = subprocess.check_output(settings.PID, shell=True)
        if ret:
            return int(ret)
        else:
            return 0

    def stop_index(self):
        subprocess.check_call('kill -9 %s' % self.get_pid(), shell=True)

    def start_index(self):
        subprocess.check_call(settings.START_INDEX, shell=True)
