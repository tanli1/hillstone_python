#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import MySQLdb
import sys
#from prettytable import PrettyTable
import prettytable


class Mysql(object):
    def __init__(self, test_db, test_table):
        self.database = test_db
        self.table = test_table
    
    def conn_table(self):
        try:
            self.conn = MySQLdb.connect("localhost", "root", "123456", "%s" %self.database,charset='utf8')
        except Exception as e:
            print "Error: connection fail!"
            return e 
        print 'Database connection success!'

    def conn_db(self):
        try:
            self.conn = MySQLdb.connect("localhost", "root", "123456", charset='utf8')
        except Exception as e:
            print "Error: connection fail!"
            return e 

    def create_databse(self):
        
        self.conn_db()
        # 使用cursor()方法获取操作游标 
        cur = self.conn.cursor()
        # 使用execute方法执行SQL语句
        try:
            cur.execute("create database %s character set utf8;" %self.database)
            cur.execute("use %s;" %self.database)
            cur.execute("create table %s(id int(11) not null auto_increment,name char(20),email char(50),password char(50),primary key (id))character set utf8;" %self.table)           
        except Exception as e:
               self.conn.rollback()   # 发生错误时回滚
               print 'Create database or table fail!'
               print e
               return e 
        self.conn.close() 
        print 'Create database and tables success!'
        
    def insert_data(self):
        ''' insert data to tables'''
       
        self.conn_table()
        # 使用cursor()方法获取操作游标 
        cursor = self.conn.cursor()
        print("Use guide: if you want to quit, please input quit")
        while True:
            # user need input name
            input_name = raw_input("Please input the name(less than or equal 20 char): ")
            if input_name == 'quit':
                break
            while len(input_name) > 20:
                input_name = raw_input("The name input is more than 20 char,please input again: ")
            # user need input email address
            input_email = raw_input("Please input the email(less than or equal 50 char): ")
            if input_email == 'quit':
                break
            while len(input_email) > 50:
                input_name = raw_input("The email input is more than 50 char,please input again: ")
            # user need input password
            input_password = raw_input("Please input the password(less than or equal 50 char): ")
            if input_password == 'quit':
                break
            while len(input_password) > 50:
                input_name = raw_input("The password input is more than 50 char,please input again: ")
            
            sql = "insert into test_table(name,email,password) values('%s','%s','%s')" %(input_name,input_email,input_password)
            try:
                sql = cursor.execute(sql)
                self.conn.commit()   # 提交到数据库执行
            except Exception as e:
                self.conn.rollback()  # 发生错误时回滚
                self.conn.close()
                return e
            print "Insert one data success!"
        self.conn.close()  # 关闭数据库连接
        
    def query_data(self):
       
        self.conn_table()
        # 使用cursor()方法获取操作游标 
        cur = self.conn.cursor()
        # 使用execute方法执行SQL语句
        sql = "select * from %s;" %self.table
        try:
            cur.execute(sql)
            result = cur.fetchall() # result is tuple
            #pt = PrettyTable()   # 
            pt = prettytable.PrettyTable()
            pt.field_names = ["id","name","email","password"]
            for row in result:
                pt.add_row(row)
            print pt
        except Exception as e:
            print "Error: unable to fecth data"
            print '%s' %e
            self.conn.close()
            return e 
        
        self.conn.close() 

    def delete_data(self):
        ''' delete data by id '''
        print("Use guide: if you want to quit, please input quit")
        input_id = ""
        while input_id != 'quit':
            input_id = raw_input("Please input the id(id is a number): ")
            if input_id == 'quit':
                break
            elif input_id.isdigit():
               
                self.conn_table()        
                # 使用cursor()方法获取操作游标 
                cur = self.conn.cursor()
                query = "select id from %s where id=%s;" %(self.table,input_id)
                query = cur.execute(query)   # 使用execute方法执行SQL语句
                if query:
                    sql = "delete from %s where id = %s" %(self.table,input_id)
                    try:
                        cur.execute(sql)
                        self.conn.commit()
                        print 'Success to delete the item: id=%s' %input_id
                    except:
                        self.conn.rollback()  # 发生错误时回滚
                        print 'Fail to delete the item: id=%s' %input_id           
                    self.conn.close() 
                else:
                    print "ID = %s id not exit,delete fail!"  %input_id
            else:
                print "Input data is not number,delete fail!"      

    def drop_database(self):
        self.conn_db()
        cur = self.conn.cursor()
        sql = "drop database %s" %(self.database)
        try:
            sql = cur.execute(sql)   # 使用execute方法执行SQL语句
        except Exception as e:
               self.conn.rollback()   # 发生错误时回滚
               print 'delete database fail!'
               print e
               return e 
        self.conn.close()





def main():

    sql = Mysql('test_db','test_table')
    if 'get' in sys.argv[1]:
        sql.query_data()
    elif 'insert' in sys.argv[1]:
        sql.insert_data()
    elif 'delete' in sys.argv[1]:
        sql.delete_data()
    elif 'create' in sys.argv[1]:
        sql.create_databse()
    elif 'drop' in sys.argv[1]:
        sql.drop_database()
    else:
        print "The argument %s is wrong,right argument is 'get', 'insert', 'delete', 'create', 'drop'" %sys.argv[1]
    
if __name__ == '__main__':
    main()

