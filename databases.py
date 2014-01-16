__author__ = 'jiahuixing'
# -*- coding: utf-8 -*-

import logging
from time import sleep

#import config as conf
import MySQLdb
import _mysql_exceptions

from commonLib import debug as debug


class Databases():
    __conn_w = None
    __conn_r = None

    def __init__(self, db, host_w, port_w, user_w, passwd_w, host_r=None, port_r=None, user_r=None, passwd_r=None):
        self.__db = db
        self.__host_w = host_w
        self.__port_w = port_w
        self.__user_w = user_w
        self.__passwd_w = passwd_w
        if None == host_r:
            self.__host_r = host_w
        if None == port_r:
            self.__port_r = port_w
        if None == user_r:
            self.__user_r = user_w
        if None == passwd_r:
            self.__passwd_r = passwd_w

        if not self.connect_to_db():
            logging.error("db connect failed")
            assert False

    def __del__(self):
        self.__conn_w.close()
        self.__conn_r.close()

    def connect_to_db(self):
        try:
            self.__conn_w = MySQLdb.connect(host=self.__host_w,
                                            port=self.__port_w,
                                            user=self.__user_w,
                                            passwd=self.__passwd_w,
                                            db=self.__db,
                                            charset='utf8')
        except Exception, e:
            logging.error(e)
            return "%s:%s %s" % (self.__host_w, self.__port_w, self.__db)

        try:
            self.__conn_r = MySQLdb.connect(host=self.__host_r,
                                            port=self.__port_r,
                                            user=self.__user_r,
                                            passwd=self.__passwd_r,
                                            db=self.__db,
                                            charset='utf8')
        except Exception, e:
            logging.error(e)
            return "%s:%s %s " % (self.__host_r, self.__port_r, self.__db)

        return True

    def __reconnect_to_write_db(self):
        try:
            self.__conn_w = MySQLdb.connect(host=self.__host_w,
                                            port=self.__port_w,
                                            user=self.__user_w,
                                            passwd=self.__passwd_w,
                                            db=self.__db,
                                            charset='utf8')
        except Exception, e:
            logging.error(e)
            sleep(60)
            self.__reconnect_to_write_db()

    def __reconnect_to_read_db(self):
        """

        @param self:
        """
        try:
            self.__conn_r = MySQLdb.connect(host=self.__host_r,
                                            port=self.__port_r,
                                            user=self.__user_r,
                                            passwd=self.__passwd_r,
                                            db=self.__db,
                                            charset='utf8')
        except Exception, e:
            logging.error(e)
            sleep(60)
            self.__reconnect_to_read_db()

    def query(self, sql, args=None):
        cursor = self.__conn_r.cursor()
        try:
            count = cursor.execute(sql, args)
            debug('count=%s' % count)
        except _mysql_exceptions.OperationalError, connect_error:
            logging.error("Exception %s, sql = %s, args = %s" % (connect_error, sql, args))
            if connect_error[0] == 2006:
                self.__reconnect_to_read_db()
                return self.query(sql, args)
            else:
                return ()
        except Exception, e:
            logging.error("Exception %s , sql = %s, args = %s" % (e, sql, args))
            return ()

        return cursor.fetchall()

    def execute(self, sql, args=None):
        """

        @param self:
        @param sql:
        @param args:
        @raise:
        """
        cursor = self.__conn_w.cursor()
        try:
            affects = cursor.execute(sql, args)
            debug('affects=%s' % affects)
        except _mysql_exceptions.OperationalError, connect_error:
            logging.error("Exception %s , sql = %s , args = %s" % (connect_error, sql, args))
            if connect_error[0] == 2006:
                self.__reconnect_to_write_db()
                self.execute(sql, args)
            else:
                raise
        except Exception, e:
            logging.error("Exception %s, sql = %s, args = %s" % (e, sql, args))
            raise

    def my_escape(self, string):
        """

        @param self:
        @param string:
        @return:
        """
        return self.__conn_w.escape_string(string)
