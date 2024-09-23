#06testround.py

# 변수다중선언
a,b, ret = 9 , 4, 0
mok = 34.5697
print(mok)
print('%d' %(mok))  # 실수이지만  정수 34출력
print('%f' %(mok))  # %f는 자릿수 지정안하면 6자릿수까지 출력
print('%.2f' %(mok)) # %f는 자릿수 지정
print(round(mok,2)) # 내장함수  round(값,2)

#내장함수 
# print() , int(), type() , input('안내문') , str(), sum()
# round(데이터,실수자릿수2)

# %자릿수d정수 %자릿수f실수
# print('%d * %d = %d' %(a,b,ret))


#  곱하기 연산처리
# ret = a*b

# print(ret) # print(변수, '문자' , ~~) , 나열식
# print('7*4=28') 은 절대아님
# print(a,'*',b, '=', ret)

# print( '%d정수 %s문자열 %f실수 %c문자'%(데이터) )
# print('%d * %d = %d' %(a,b,ret))

# print( '{} * {} = {}' .format(a,b,ret) )
# print('{} * {} = {}'.format(a,b,ret))

# print(f'{변수및값}')
# print(f'{a} * {b} = {ret}')