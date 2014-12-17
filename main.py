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
    s1 = Server(1)
    s2 = Server(2)
    s3 = Server(3)
    s4 = Server(4)
    listener = Listener()
    listener.start()
    time.sleep(randint(2,9))
    s1.start()
    time.sleep(randint(2,9))
    s2.start()
    time.sleep(randint(2,9))
    s3.start()
    time.sleep(randint(2,9))
    s4.start()
    s1.join()
    s2.join()
    s3.join()
    s4.join()
    
    
