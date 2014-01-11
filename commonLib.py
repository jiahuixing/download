__author__ = 'tracy'

import sys
import time
import os

TYPE_INT = 'int'
TYPE_STR = 'str'

TIME_HMS = 'hms'
TIME_YMD = 'ymd'


def debug(msg):
    """

    :param msg:
    """
    print('******%s******' % msg)


def getDate():
    """


    :return:
    """
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        block = '.'
        year, mon, day = time.strftime('%Y'), time.strftime('%m'), time.strftime('%d')
        year = year[-1]
        mon = str(int(mon))
        day = str(int(day))
        version = year + block + mon + block + day
    return version


def inputValue(input_length=1, input_type=TYPE_INT):
    """

    :param input_length:
    :param input_type:
    :return:
    """
    debug('input_type=%s' % input_type)
    input_info = sys.stdin.read(input_length)
    if input_type == TYPE_INT:
        if input_info.isdigit():
            return input_info
        else:
            inputValue(input_length, input_type)
    elif input_type == TYPE_STR:
        if input_type in ['']:
            return input_info
        else:
            inputValue(input_length, input_type)


def setNumValue(value=0):
    """

    :param value:
    """
    global num
    num = value


def getNumValue():
    """


    :return:
    """
    return num


def setStrValue(value=''):
    """

    :param value:
    """
    global string
    string = value


def getStrValue():
    """


    :return:
    """
    return string


def runCommand(cmd):
    """

    :param cmd:
    """
    os.system(cmd)


def getSysArgv(index):
    """

    :param index:
    """
    return sys.argv[index - 1]


def getTime(time_type=TIME_HMS):
    """

    :param time_type:
    """
    block = '-'
    if time_type == TIME_HMS:
        return (time.strftime('%H') + block + time.strftime('%M') + block + time.strftime('%S'))
    elif time_type == TIME_YMD:
        return (time.strftime('%Y') + block + time.strftime('%m') + block + time.strftime('%d'))