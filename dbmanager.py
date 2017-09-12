# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
from mysql.connector import errorcode
from mysql.connector import pooling
import time


class CrawlDatabaseManager:
    DB_NAME = 'jc_crawl'
    SERVER_IP = '172.16.0.116'

    TABLES = {}

    def __init__(self, max_num_thread):
        # connect mysql server
        try:
            cnx = mysql.connector.connect(host=self.SERVER_IP, user='root', password='jcplanb.com')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print "Something is wrong with your user name or password"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print "Database does not exist"
            else:
                print 'Create Error ' + err.msg
            exit(1)

        cursor = cnx.cursor()

        # use database, create it if not exist
        try:
            cnx.database = self.DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                # create database and table
                self.create_database(cursor)
                cnx.database = self.DB_NAME
                self.create_tables(cursor)
            else:
                print err
                exit(1)
        finally:
            cursor.close()
            cnx.close()

        dbconfig = {
            "database": self.DB_NAME,
            "user": "root",
            "password": "jcplanb.com",
            "host": self.SERVER_IP,
        }
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                                   pool_size=max_num_thread,
                                                                   **dbconfig)

    # create databse
    def create_database(self, cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print "Failed creating database: {}".format(err)
            exit(1)

    def create_tables(self, cursor):
        for name, ddl in self.TABLES.iteritems():
            try:
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print 'create tables error ALREADY EXISTS'
                else:
                    print 'create tables error ' + err.msg
            else:
                print 'Tables created'

    ##########
    ## crawl_catorgy
    # initial crawl_catorgy
    def init_catorgy_url(self):
        print('------')
        con = self.cnxpool.get_connection()
        cursor = con.cursor()
        print(time.strftime("%H%M%S", time.localtime()))
        try:
            if time.strftime("%H%M%S", time.localtime()) < '013000':
                user_init = 'update crawl_catorgy SET crawl_status="new"'
            elif (int(time.strftime("%H", time.localtime())) % 3) == 0:
                # user_init = 'update crawl_catorgy SET crawl_status="new" where crawl_status = "downloading"'
                user_init = 'update crawl_catorgy SET crawl_status="new"'
            else:
                user_init = None

            if user_init <> None:
                cursor.execute(user_init)
                con.commit()
        except mysql.connector.Error as err:
            print 'user_init() ' + err.msg
            return
        finally:
            cursor.close()
            con.close()

    # get an web catorgy from queue
    def dequeue_catorgy_url(self):
        con = self.cnxpool.get_connection()
        cursor = con.cursor(dictionary=True)
        try:
            # use select * for update to lock the rows for read
            query = (
            "SELECT `id`, `catorgy_url` FROM crawl_catorgy WHERE crawl_status='new' ORDER BY `id` ASC LIMIT 1 FOR UPDATE")
            cursor.execute(query)
            if cursor.rowcount is 0:
                return None
            row = cursor.fetchone()
            if row is None:
                return None
            update_query = ("UPDATE crawl_catorgy SET `crawl_status`='downloading' WHERE `id`=%d") % (row['id'])
            cursor.execute(update_query)
            con.commit()
            return row
        except mysql.connector.Error as err:
            # print 'dequeueUrl() ' + err.msg
            return None
        finally:
            cursor.close()
            con.close()

    def finish_catorgy_url(self, index):
        con = self.cnxpool.get_connection()
        cursor = con.cursor()
        try:
            update_query = ("UPDATE crawl_catorgy SET `crawl_status`='done' WHERE `id`=%d") % (index)
            cursor.execute(update_query)
            con.commit()
        except mysql.connector.Error as err:
            # print 'finishUrl() ' + err.msg
            return
        finally:
            cursor.close()
            con.close()

    # enqueue url insert table
    def enqueue_crawl_url(self, mid, kw, **kwargs):
        print('------')
        con = self.cnxpool.get_connection()
        cursor = con.cursor(buffered=True)
        try:
            keys = 'url_md5'
            values = (mid,)
            values_stmt = '%s'

            for key in kwargs:
                keys += ', ' + key
                values_stmt += ', %s'
                values += (kwargs[key],)
            add_doc_info = ("INSERT INTO crawl_url (%s) VALUES ") % (keys)
            add_doc_info += '(' + values_stmt + ')'

            update_kw = u'UPDATE crawl_url SET kwords = IF(kwords is NULL, "%s", IF(kwords like "%%%s%%", kwords, CONCAT(kwords, ",%s"))) where url_md5 = "%s"' % (
            kw, kw, kw, mid)
            print(update_kw)
            query = ('SELECT `id` FROM crawl_url WHERE url_md5="%s"') % (mid)
            print(query)

            cursor.execute(query)
            print(query)
            print(cursor.rowcount)
            if cursor.rowcount < 1:
                print(add_doc_info)
                print(values)
                cursor.execute(add_doc_info, values)
            else:
                cursor.execute(update_kw)
                print(update_kw)

            # cursor.execute(add_doc_info, values)
            # cursor.execute(update_kw)
            # commit this transaction, please refer to "mysql transaction" for more info
            con.commit()
        except mysql.connector.Error as err:
            print 'insert_weibo() ' + err.msg
            return
        finally:
            cursor.close()
            con.close()

    ##########
    ## crawl_url
    # initial crawl_url
    def init_crawl_url(self):
        con = self.cnxpool.get_connection()
        cursor = con.cursor()
        try:
            if time.strftime("%H%M%S", time.localtime()) < '013000':
                user_init = 'update crawl_url SET status_crawl="new" where status_crawl = "downloading"'
            else:
                user_init = None

            if user_init <> None:
                cursor.execute(user_init)
                con.commit()
        except mysql.connector.Error as err:
            print 'crawl_url_init() ' + err.msg
            return
        finally:
            cursor.close()
            con.close()

    # get an web catorgy from queue
    def dequeue_crawl_url(self):
        con = self.cnxpool.get_connection()
        cursor = con.cursor(dictionary=True)
        try:
            # use select * for update to lock the rows for read
            query = (
            "SELECT `id`, `url_md5`, `url`, `catorgy_url` FROM crawl_url WHERE status_crawl='new' ORDER BY `id` ASC LIMIT 1 FOR UPDATE")
            cursor.execute(query)
            if cursor.rowcount is 0:
                return None
            row = cursor.fetchone()
            if row is None:
                return None
            update_query = ("UPDATE crawl_url SET `status_crawl`='downloading' WHERE `id`=%d") % (row['id'])
            cursor.execute(update_query)
            con.commit()
            return row
        except mysql.connector.Error as err:
            print 'dequeueUrl() ' + err.msg
            return None
        finally:
            cursor.close()
            con.close()

    def finish_crawl_url(self, index):
        con = self.cnxpool.get_connection()
        cursor = con.cursor()
        try:
            update_query = ("UPDATE crawl_url SET `status_crawl`='done' WHERE `id`=%d") % (index)
            cursor.execute(update_query)
            con.commit()
        except mysql.connector.Error as err:
            # print 'finishUrl() ' + err.msg
            return
        finally:
            cursor.close()
            con.close()
