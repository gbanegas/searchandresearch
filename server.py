'''
Created on 16 Dec 2014

@author: gustavo
'''

import threading 
import time

class Server(threading.Thread):
    USER_IDS = ['5352b590-05ac-11e3-9923-c3e7d8408f3a', 'f85f124a-05cd-11e3-8a11-a8206608c529', '5352b590-05cd-11e3-8a11-9923-c3e7d84005cd']

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):


