# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 16:11
# @Author  : Tom_zc
# @FileName: common.py.py
# @Software: PyCharm

import subprocess
import time
import traceback


def execute_cmd(cmd, timeout=30, err_log=False):
    """execute cmd"""
    try:
        p = subprocess.Popen(cmd.split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        t_wait_seconds = 0
        while True:
            if p.poll() is not None:
                break
            if timeout >= 0 and t_wait_seconds >= (timeout * 100):
                p.terminate()
                return -1, "", "execute_cmd exceeded time {} seconds in executing".format(timeout)
            time.sleep(0.01)
            t_wait_seconds += 1
        out, err = p.communicate()
        ret = p.returncode
        if ret != 0 and err_log:
            print("execute_cmd return {}, std output: {}, err output: {}.".format(ret, out, err))
        return ret, out, err
    except Exception as e:
        return -1, "", "execute_cmd exceeded raise, e={}, trace={}".format(str(e), traceback.format_exc())
