# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:58:30 2018

@author: zmddzf
"""

import clean
import model
import spider
import time
from queue import Queue
import threading

lock = threading.Lock()

#建立数据库连接
db = model.model('dzf', '123456', '39.108.102.21')

#拆分URL格式
partialURL1 = 'https://movie.douban.com/subject/1293908/comments?start='
partialURL2 = '&limit=20&sort=new_score&status=P'

#设置网页解析器pattern
pattern1 = '<p class="">(.+?)</p>'
pattern2 = '<span class="allstar(.*?) rating" title="(.+?)"></span>'

#由URL模式生成URL表
URLlist = [partialURL1+str(i)+partialURL2 for i in range(0, 200, 20)]

#将URL表交由URL管理器
url_manager = spider.URLmanager(URLlist)

#将数据存入数据库
def SendData(db, x1, x2):
    
    while True:
        if x1.empty() is False:
            xx1 = x1.get()
            xx2 = x2.get()
            for item in zip(xx2, xx1):
                score = item[0][0]
                score = int(score)
                rate = item[0][1]
                comment = clean.clean(item[1])
                comment.filter_punctuation()
                comment.filter_emoji()
                comment.wordcut()
                db.send_sql("insert into movie_comments.comments(scores, rates, comments) values('%s','%s','%s')" %(score, rate, comment.sent))
        else:
            break

#该函数为主函数，每爬取三个页面开始存入数据库，防止被ban
def main(url_manager, db):
    x1 = Queue()
    x2 = Queue()
    flag = 0
    while True:
        if url_manager.isempty() is False:
            try:
                html = spider.WebDownloader(url_manager.get_URL())
                x1.put(spider.WebParser(html, pattern1))
                x2.put(spider.WebParser(html, pattern2))
                print('爬取成功！')
            except:
                pass
        else:
            break
        flag += 1
        if flag % 3 == 0:
            #线程锁
            lock.acquire()
            try:
                SendData(db, x1, x2)
            finally:
                #释放线程锁
                lock.release()



main(url_manager, db)

#与数据库断开连接
db.close()














