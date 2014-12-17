#!/usr/bin/pyton 
'''
Created on 15 Dec 2014

@author: gustavo
'''

import time
from random import randint

from parse import Parse
from listener import Listener
from server import Server

if __name__ == "__main__":
    print 'Creating parse'
    listener = Listener()
    listener.start()
    list_of_servers = []
    for i in xrange(4):
        list_of_servers.append(Server(i))
    
    for s in list_of_servers:
        s.start()
        time.sleep(randint(2,9))

    for s in list_of_servers:
        s.join()

    
    
