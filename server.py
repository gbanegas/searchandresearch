'''
Created on 16 Dec 2014

@author: gustavo
'''

import threading 
import time
import os
from random import randint

class Server(threading.Thread):
    USER_IDS = ['5352b590-05ac-11e3-9923-c3e7d8408f3a', 'f85f124a-05cd-11e3-8a11-a8206608c529', '5352b590-05cd-11e3-8a11-9923-c3e7d84005cd']
    INPUT = ['177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] \"GET /meme.jpg HTTP/1.1\" 200 2148 \"-\"\"userid=','177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] \"GET /teste.jpg HTTP/1.1\" 200 2148 \"-\"\"userid=','127.0.0.1 - - [15/Aug/2013:13:54:38 -0300] \"GET /meme.jpg HTTP/1.1\" 200 2148 \"-\"\"userid=']
    identificador = 0
    file_to_write = None
    filename = None
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.identificador = id
        path = 'server_'+ str(self.identificador)
        f = 'server_' + str(self.identificador)+'.log'
        if not os.path.exists(path):
            os.makedirs(path)
        self.filename = os.path.join(path, f)
        self.file_to_write= open(self.filename, 'w')

    def run(self):
        while(True):
            user_index = randint(0,2)
            input_index = randint(0,2)
            self.file_to_write= open(self.filename, 'w')
            log_input = self.INPUT[input_index] + self.USER_IDS[user_index] + '\"' + '\n'
            self.file_to_write.write(log_input)
            self.file_to_write.close()
            print log_input
            time.sleep(randint(2,9))



s1 = Server(1);
s2 = Server(2);
s3 = Server(3);
s4 = Server(4);

s1.start();
s2.start();
s3.start();
s4.start();


s1.join();
s2.join();
s3.join();
s4.join();



