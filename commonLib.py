__author__ = 'tracy'
# -*- coding: utf-8 -*-

import sys
import time
import os

TYPE_INT = 'int'
TYPE_STR = 'str'

TIME_HMS = 'hms'
TIME_YMD = 'ymd'


#参数
TIMEOUT = 5
MAIN_PAGE = 'http://ota.n.miui.com/ota/'
CHOOSE_T_SYS = 'sys.argv'
CHOOSE_T_IN = 'input'

#shell 命令
DOWNLOAD_COMMAND = 'wget '
FLASH_SCRIPT = './flash.sh '

#机型信息
X1 = 'mione_plus_'
X2 = 'aries_'
X2_ALPHA = 'aries_alpha_'
X2A = 'taurus_'
X2A_ALPHA = 'taurus_alpha_'
X3_TD = 'pisces_'
X3_W = 'cancro_'
HM2_TD = 'wt93007_'
HM2_W = 'HM2013023_'

CHOOSE = [X1, X2, X2_ALPHA, X2A, X2A_ALPHA, X3_TD, X3_W, HM2_TD, HM2_W]

MIDDLE = 'images_'


#re匹配
IMAGES_SUF = r'_4.[0-9]{1}_[a-zA-Z0-9]{10}.tar'


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


def get_index(ele, list_name=None):
    """

    @param ele:
    @param list_name:
    """
    if not list_name: list_name = []
    index = None
    if ele in list_name:
        for mem in list_name:
            if mem == ele:
                index = list_name.index(mem) + 1
                break
    else:
        index = None
    return index


def get_info(info, list_name):
    """

    @param info:
    @param list_name:
    @return:
    """
    m_info = info
    wrap = '\n'
    for mem in list_name:
        index = get_index(mem, list_name)
        m_info = '%s%s:%s%s' % (m_info, index, mem, wrap)

    return m_info



