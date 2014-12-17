'''
Created on 15 Dec 2014

@author: gustavo
'''

import random
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from parse import Parse

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parse = Parse('entrada.txt')

    def test_parse(self):
        self.parse.parse_file()
        path = os.getcwd() + '/server_1/5352b590-05ac-11e3-9923-c3e7d8408f3a'
        self.assertTrue(os.path.isfile(path))
        f = open(path,'r')
        line = f.readlines()
        self.assertEqual(line[0], '177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] \"GET /meme.jpg HTTP/1.1\" 200 2148 \"-\" \"userid=5352b590-05ac-11e3-9923-c3e7d8408f3a\"\n')
        self.assertEqual(line[2], '177.126.180.83 - - [15/Aug/2013:13:57:48 -0300] \"GET /lolcats.jpg HTTP/1.1\" 200 5143 \"-\" \"userid=5352b590-05ac-11e3-9923-c3e7d8408f3a\"\n')

    def test_parse_error(self):
        self.parse.parse_file()
        path = os.getcwd() + '/server_1/f85f124a-05cd-11e3-8a11-a8206608c529'
        self.assertTrue(os.path.isfile(path))
        f = open(path,'r')
        line = f.readlines()
        self.assertNotEqual(line[0], '177.126.180.83 - - [15/Aug/2013:13:54:38 -0300] \"GET /meme.jpg HTTP/1.1\" 200 2148 \"-\" \"userid=5352b590-05ac-11e3-9923-c3e7d8408f3a\"\n')

        
       
        

if __name__ == '__main__':
    unittest.main()