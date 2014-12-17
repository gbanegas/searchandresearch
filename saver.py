'''
Created on 15 Dec 2014

@author: gustavo
'''
import os

class Saver(object):

    def save_in_file(self, user_id, l, path='/server_1/'):
        path = os.getcwd() + path
        filename = path + user_id
        f = open(filename,'w')
        for entrace in l:
            f.write(entrace.server_entrace+'\n')
        f.close()
        


