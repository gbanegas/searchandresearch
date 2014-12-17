import random
import time

class RandomDate(object):

    def str_time_prop(self, start, end, format, prop):
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(format, time.localtime(ptime))

    def random_date(self, start, end, prop):
        return self.str_time_prop(start, end, '%d/%b/%Y:%H:%M:%S', prop)




ra = RandomDate()
print ra.random_date("1/Aug/2008:1:30:00", "1/Nov/2014:4:50:00", random.random())