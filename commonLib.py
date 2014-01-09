__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import sys
import time

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


def test():
    pass