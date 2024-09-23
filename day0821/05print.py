#04tprint.py

# 변수선언
msg = 97234
print('{}'.format(msg)) # 정석 97234
print('{:>10,}'.format(msg)) # 총10자릿수 >오른쪽맞춤
print('{:<10,}'.format(msg)) # 총10자릿수 <왼쪽맞춤
print('{:^10,}'.format(msg)) # 총10자릿수 ^중앙맞춤

print('_'*100)
print('{:0>10,}'.format(msg))  # 000097,234
print('{:*>10,}'.format(msg))  # ****97,234
print('{:,}'.format(msg))      #97,234










'''
print(ret) # print(변수, '문자' , ~~) , 나열식
# print('7*4=28') 은 절대아님
print(a,'*',b, '=', ret)

# print( '%d정수 %s문자열 %f실수 %c문자'%(데이터) )
print('%d * %d = %d' %(a,b,ret))

# print( '{} * {} = {}' .format(a,b,ret) )
print('{} * {} = {}'.format(a,b,ret))

# print(f'{변수및값}')
print(f'{a} * {b} = {ret}')
'''
