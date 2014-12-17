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

        self.__sorter__()
        #self.__print_entrace__()
            

    def __get_user_id(self,line):
        location = line.find(self.USER_ID)
        sub = line[location:len(line)].replace('"','')
        user_id = sub.replace(self.USER_ID+"=",'').strip()
        self.mp[user_id].append(Entrace(line))
       

    def __sorter__(self):

        for obj in self.mp:
            l = self.mp[obj]
            l.sort(cmp=lambda x,y: cmp(x.date, y.date))
            for i in l:
                print i.server_entrace
            self.mp[obj] = l
           


    def __print_entrace__(self):
        for obj in self.mp:
            for i in self.mp[obj]:
                print i.server_entrace


            
        
