'''
Created on 15 Dec 2014

@author: gustavo
'''

import threading 
import os, sys, time, subprocess
from parse import Parse

class Listener(threading.Thread):
    paths_to_listen = ['/server_1/', '/server_2/', '/server_3/', '/server_4/']

    def __init__(self):
        self.parse = Parse()

    def run(self):
        time.sleep(2)
        for path_to_watch in paths_to_listen:
            after = files_to_timestamp(path_to_watch)
            added = [f for f in after.keys() if not f in before.keys()]
            removed = [f for f in before.keys() if not f in after.keys()]
            modified = []
            fileName = ""
            for f in before.keys():
                if not f in removed:
                    if os.path.getmtime(f) != before.get(f):
                        modified.append(f)
                        fileName = f
            if modified:
                if fileName.endswith(".log"):
                    print fileName

    def files_to_timestamp(path):
        files = [os.path.join(path, f) for f in os.listdir(path)]
        return dict ([(f, os.path.getmtime(f)) for f in files])
