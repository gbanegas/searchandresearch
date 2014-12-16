#!/usr/bin/pyton 
'''
Created on 15 Dec 2014

@author: gustavo
177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] "GET /meme.jpg HTTP/1.1" 200 2148 "-" "userid=5352b590-05ac-11e3-9923-c3e7d8408f3a"
'''

import re
import datetime

class Entrace(object):
    server_entrace = None
    date = None

    def __init__(self, server_entrace):
        self.server_entrace = server_entrace
        self.__break__()
       


    def __break__(self):
        match = re.search(r'(\d+/\w+/\d+:\d+:\d+:\d+)',self.server_entrace)
        date = datetime.datetime.strptime(match.group(0),"%d/%b/%Y:%H:%M:%S")
        print date

