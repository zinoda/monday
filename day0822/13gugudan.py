#13gugudan.py

data = input('구구단입력>>> ')
dan = int(data)
for k in range(1, 10,1) :
    print(dan, ' *',k,'=', (dan*k))


# dan = 7
# for k in range(1, 10,1) :
#     print(dan, ' *',k,'=', (dan*k))  # 구구단적용

print()
print('구구단 연습')

'''
파이썬 화면모니터 출력 print ( '안내문' , 값)
파이썬 키보드자판 입력 input ( '안내문')
파이썬 키보드입력데이터 문자로인식
int("1200") 숫자 120
'''

# a = '120'
# b = '75'
# print(a+b) #12075

# c = int(a) + int(b)  #int정수=integer
# print(int(a)+ int(b)) #int정수=integer
# print(c)

# # 파이썬 내장함수
# # print() , int() , round() , input() , str() , sum()
