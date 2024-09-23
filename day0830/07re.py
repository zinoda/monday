# 07re.py
import re


# url = 'www.google.com'
# print(url.split(','))
# print(''.join(url))

msg = 'my best blue myjava my cherry my phthon my'
x = re.findall('my' , msg)
y = re.findall('blue' , msg)
z = re.findall('red', msg)
print(x)
print(y)
print(z) # 에러 대신 [] 출력

info1 = re.findall('[a-zA-Z]{3,7}' , msg)
info2 = re.findall('[a-zA-Z0-9]{3,7}' , msg)
print(info1)
print(info2)
print()

#msg  변수에 새로운 내용을 덮어씌우는 재할당
msg = 'my best &%(@ 245 오렌지 수박 cherry as tea'

result1 = re.findall('[\w]' , msg)
result2 = re.findall('[\W]' , msg)
result3 = re.findall('[a-zA-Z0-9가-힣]', msg)

print(result1)
print(result2)
print(result3)

my = re.findall('[a-zA-Z]{7,10}' , msg)
if my :
    print(my)
else :
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터가 없습니다')