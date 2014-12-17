'''
Created on 15 Dec 2014

@author: gustavo
'''

import threading 
import time
import fcntl
import os
import signal
import logging
from parse import Parse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Listener(threading.Thread):
  
    def __init__(self):
        threading.Thread.__init__(self)
        event_handler = MyHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, ".", recursive=True)
        #observer.start()
        self.observer.start()

    def run(self):
        time.sleep(2)
       

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.parse = Parse()
        if(event.src_path.endswith(".log")):
            self.parse.set_file_path(event.src_path)
            self.parse.parse_file()
    