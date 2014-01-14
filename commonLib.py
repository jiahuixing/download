__author__ = 'tracy'
# -*- coding: utf-8 -*-

#system lib
import sys
import time
import os

#3rd party lib
import MySQLdb

#my lib
from Info import *


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
            set_num_value(int(input_info))
        else:
            input_value(input_length, input_type)
    elif input_type == TYPE_STR:
        if input_type.isalpha():
            set_str_value(input_info)
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


def get_index(element, list_name=None):
    """

    @param element:
    @param list_name:
    """
    if not list_name: list_name = []
    index = None
    if element in list_name:
        for mem in list_name:
            if mem == element:
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


def connect_to_db(dbinfo=MY_DB_INFO):
    """

    @param dbinfo:
    """
    global conn, cursor
    my_host = MY_DB_INFO['host']
    my_user = MY_DB_INFO['user']
    my_passwd = MY_DB_INFO['passwd']
    conn = MySQLdb.connect(host=my_host, user=my_user, passwd=my_passwd, db="test", charset="utf8")
    cursor = conn.cursor()


def close_db():
    """


    """
    conn.close()

