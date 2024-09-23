#replace.py

#문자, 문자열변경 replace(변경대상,새로운대상)
#문자,문자열 공백제거 strip

info = 'my best friend gildong'

myret1 = info.replace('best' , 'coffee')
print(myret1)
myret2 = info.replace(' ','')
print(myret2)

msg = 'it is a best python   '
x='aaa'
y='bbb'

# print(x+msg+y) #연결
print(x + msg.lstrip()+y)  # msg 왼쪽 공백 제거
print(x + msg.rstrip()+y)  # msg 오른쪽 공백 제거
print(x + msg.strip()+y) 