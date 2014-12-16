'''
Created on 15 Dec 2014

@author: gustavo
'''
from collections import defaultdict
from entrace import Entrace

class Parse(object):
    USER_ID = 'userid'

    fileToRead = open('entrada.txt', 'r')
    mp = defaultdict(list)

    def parse_file(self):
        for line in self.fileToRead:
            self.__get_user_id(line)
            

    def __get_user_id(self,line):
        location = line.find(self.USER_ID)
        sub = line[location:len(line)].replace('"','')
        user_id = sub.replace(self.USER_ID+"=",'').strip()
        self.mp[user_id].append(Entrace(line))
        print self.mp 
        
