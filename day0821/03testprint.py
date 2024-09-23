#02testprint.py

# 변수 하나씩선언, 다중선언
# a = 7
# b = 4
# ret = 0   

a,b, ret = 9 , 4, 0

ret = a*b
print(ret) # print(변수, '문자' , ~~) , 나열식
# print('7*4=28') 은 절대아님
print(a,'*',b, '=', ret)

# print( '%d정수 %s문자열 %f실수 %c문자'%(데이터) )
print('%d * %d = %d' %(a,b,ret))

# print( '{} * {} = {}' .format(a,b,ret) )
print('{} * {} = {}'.format(a,b,ret))

# print(f'{변수및값}')
print(f'{a} * {b} = {ret}')