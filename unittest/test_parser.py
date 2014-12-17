'''
Created on 15 Dec 2014

@author: gustavo
'''

import random
import unittest
from parse import Parse

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parse = Parse()

    def test_parse(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

if __name__ == '__main__':
    unittest.main()