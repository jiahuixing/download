__author__ = 'tracy'

import sys
import time


TYPE_INT = 'int'
TYPE_STR = 'str'


def debug(msg):
    print('******%s******' % msg)


def getDate():
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
    global num
    num = value


def getNumValue():
    return num


def setStrValue(value=''):
    global string
    string = value


def getStrValue():
    return string
