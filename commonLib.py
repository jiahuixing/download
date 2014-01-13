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


def get_date():
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


def input_value(input_length=1, input_type=TYPE_INT):
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
            input_value(input_length, input_type)
    elif input_type == TYPE_STR:
        if input_type in ['']:
            return input_info
        else:
            input_value(input_length, input_type)


def set_num_value(value=0):
    """

    :param value:
    """
    global num
    num = value


def get_num_value():
    """


    :return:
    """
    return num


def set_str_value(value=''):
    """

    :param value:
    """
    global string
    string = value


def get_str_value():
    """


    :return:
    """
    return string


def run_command(cmd):
    """

    :param cmd:
    """
    os.system(cmd)


def get_sys_argv(index):
    """

    :param index:
    """
    return sys.argv[index - 1]


def get_time(time_type=TIME_HMS):
    """

    :param time_type:
    """
    block = '-'
    if time_type == TIME_HMS:
        hour = time.strftime('%H')
        mini = time.strftime('%M')
        sec = time.strftime('%S')
        hms = hour + block + mini + block + sec
        return hms
    elif time_type == TIME_YMD:
        year = time.strftime('%Y')
        month = time.strftime('%m')
        day = time.strftime('%d')
        ymd = year + block + month + block + day
        return ymd