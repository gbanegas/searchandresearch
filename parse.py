'''
Created on 15 Dec 2014

@author: gustavo
'''

class Parse(object):
    USER_ID = 'userid'

    fileToRead = open('entrada.txt', 'r')

    def parse_file(self):
        for line in self.fileToRead:
            __user_id = self.__get_user_id(line)
            print __user_id

    def __get_user_id(self,line):
        location = line.find(self.USER_ID)
        sub = line[location:len(line)].replace('"','')
        return sub.replace(self.USER_ID+"=",'')
        
