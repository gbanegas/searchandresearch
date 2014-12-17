'''
Created on 15 Dec 2014

@author: gustavo
'''
import os

class Saver(object):

    def save_in_file(self, user_id, l, path=None):
        filename = user_id
        if(path <> None):
            if not os.path.exists(path):
                os.makedirs(path)
            filename = os.path.join(path, f)
        f = open(filename,'w')
        for entrace in l:
            f.write(entrace.server_entrace+'\n')
        f.close()
        


