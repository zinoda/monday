# 08 test date time.py

import time
#import detetime                #datetime.datetime.now()
import datetime 

my = time.localtime()
print(my)
print(my.tm_year,'년')
print(my.tm_mon,'월')
print(my.tm_mday,'일')
print(my.tm_wday)  #0월 1화 2수 3목 4금 5토 6일
time.sleep(0.5)
print()

dt = datetime.datetime.now()
print(dt)

time.sleep(0.3)
print('aaaaaa')
time.sleep(0.3)
print('bbbbbb')
time.sleep(0.3)
print('cccccc')