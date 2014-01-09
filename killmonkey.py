__author__ = 'jiahuixing'

import os
import sys

def kill_monkey():
    """

        """
    pid = get_monkey_pid()
    if pid:
        kill_cmd = 'adb shell kill ' + pid
        print(kill_cmd)
        os.system(kill_cmd)
    else:
        print('no monkey pid')


def get_monkey_pid():
    """

        """
    pids_cmd = 'adb shell ps | grep com.android.commands.monkey'
    result = os.popen(pids_cmd)
    for line in result.readlines():
        line = line.strip()
        if line != '':
            print(line)
            line = line.split()
            print(line)
            pid = line[1]
            print(pid)
            return pid


if __name__=='__main__':

    kill_monkey()