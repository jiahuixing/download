__author__ = 'tracy'

import urllib

from commonLib import *
from Info import *

import MySQLdb


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


def test_mysql_db():
    my_host = MY_DB_INFO['host']
    my_user = MY_DB_INFO['user']
    my_passwd = MY_DB_INFO['passwd']
    # db = MySQLdb.Connect(host=my_host, user=my_user, passwd=my_passwd)
    db = MySQLdb.connect(host=my_host, user=my_user, passwd=my_passwd)
    print(type(db))
    # assert isinstance(db, MySQLdb.connections.Connection)
    m_cursor = db.cursor()
    print type(m_cursor)
    sql = 'show databases'
    # assert isinstance(m_cursor, MySQLdb.cursors.Cursor)
    # """:type: MySQLdb.cursors.Cursor"""
    m_cursor.execute(sql)
    print m_cursor.fetchall()


test_mysql_db()