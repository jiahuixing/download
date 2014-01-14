__author__ = 'tracy'

import urllib

from commonLib import *
from Info import *


def test_time():
    xxx = get_time(TIME_YMD)
    yyy = get_time(TIME_HMS)
    debug(xxx)
    debug(yyy)


def test_index():
    index = get_index(X1, CHOOSE)
    print(index)


def test_info():
    info = 'Pls choose the num to down the tar:\n'
    info = get_info(info, CHOOSE)
    print(info)


def test_read():
    file_name = raw_input().strip('\r').strip('\n')
    print(file_name)


def test_url():
    try:
        web = urllib.urlopen('http://ota.n.miui.com/ota/').code
        print(web)
    except IOError, err1:
        debug(err1)