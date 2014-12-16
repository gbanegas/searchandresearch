'''
Created on 16 Dec 2014

@author: gustavo
'''

import threading 
import time

class Server(threading.Thread):
    USER_IDS = ['5352b590-05ac-11e3-9923-c3e7d8408f3a', 'f85f124a-05cd-11e3-8a11-a8206608c529', '5352b590-05cd-11e3-8a11-9923-c3e7d84005cd']
    INPUT = '177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] \"GET /meme.jpg HTTP/1.1\" 200 2148 \"-\"\"userid='
    identificador = 0;
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.identificador = id;

    def run(self):
        while(True):
            print "thread "  + str(self.identificador)
            time.sleep(2)



s1 = Server(1);
s2 = Server(2);
s1.start();
s2.start();

s1.join();
s2.join();




