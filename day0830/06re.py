# 06re.py
import re


# url = 'www.google.com'
# print(url.split(','))
# print(''.join(url))

msg = 'my best% 2400 Flu.it is blue %#357cherry'

info1 = re.findall('[a-zA-Z]{3,7}' , msg)
info2 = re.findall('[a-zA-Z0-9]{3,7}' , msg)
print(info1)
print(info2)
print()

my = re.findall('[a-zA-Z]{7,10}' , msg)
if my :
    print(my)
else :
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터가 없습니다')