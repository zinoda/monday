# 08testfor.py

# 문자열,리스트출력,tuple,set,dict
# 반복데이터 사용
'''
for 변수대표 k in range(10) :
    10회 반복처리 한다 0~9까지 10회처리 
for 변수대표 k in range(1~10) :
    9회 반복처리 한다 1~9까지 9회처리
for 변수대표 k in range (1,10,1)
    9회 반복처리 한다 1~9까지 9회처리
    1씩증가일때 3번쨰 1생략

while 조건 :
    조건만족시 루프loop 처리
    무한루프처리일때 if제어문으로  break 반복탈출
'''
# for,while 연습할때 사용 a,b,hap,tot
a,b= 0,0
hap,tot=0,0

message = 'hello 길동'

print(message)
print(message)
print(message)
print(message)
print(message)
print()

for k in range(5) :
    print(k, message)
    #0부터시작~4 =5회처리
    #10진수 0~9 2진수 0,1

