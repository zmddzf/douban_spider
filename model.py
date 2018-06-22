# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:40:22 2018

@author: zmddzf
"""
import pymysql

class model:
    """
    Connect to the database and send sql command.
    
    Attributes:
        send_sql: to send sql command to the database.
        close: close the database connection.
    """
    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host
        self.db = pymysql.connect(self.host, self.username, self.password,charset = 'utf8')
        
    def send_sql(self, sql):
        cursor = self.db.cursor()
        print(sql)
        state = cursor.execute(sql)
        print(state)
        self.db.commit()
        
    def close(self):
        self.db.close()
        print('The connection has been closed')
        