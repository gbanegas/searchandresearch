'''
Created on 15 Dec 2014

@author: gustavo
'''

import threading 
from parse import Parse

class Listener(threading.Thread):

    def __init__(self):
        self.parse = Parse()