# 05 as.py

import datetime as dt
import math
import re # 정규식
import sys
my = dt.datetime.now()
print('날짜 및 시간' , my)

print()
print(dir(math))
print()
print(dir(re))


print('prefix 가상이름 ' ,sys.prefix)
print('version 버젼버젼 ' , sys.version)
print('copyright 소유 ', sys.copyright)
print('path 경로' , sys.path)