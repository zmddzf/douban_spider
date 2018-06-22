# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:19:33 2018

@author: zmddzf
"""
from urllib import request
import UA_POOL as UP
from queue import Queue
import re

"""
This is a spider library which includes:
URLmanager: a manager to control the URL queue
WebParser: a Parser to get value data/URL
WebDowloader: to download html

"""

class URLmanager:
    
    def __init__(self, URLlist):
        URL = set(URLlist)
        self.URLqueue = Queue()
        for url in URL:
            self.URLqueue.put(url)
        
    def isempty(self):
        return self.URLqueue.empty()
    
    def get_URL(self):
        if self.URLqueue.empty():
            return False
        else:
            return self.URLqueue.get()

def WebDownloader(URL):
    opener = request.build_opener()
    opener.addheaders = UP.getHEADER()
    request.install_opener(opener)
    data = request.urlopen(URL).read().decode("utf-8","ignore")
    data = data.replace('\n', '')
    return data

def WebParser(html, pattern):
    return re.findall(pattern, html, re.S)


        
        
        


