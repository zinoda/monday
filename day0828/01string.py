# 01 string.py

#str() , len()

x = 'blue'
y = 1234
print( x + str(y))  # 분리 문자 , 숫자
print(f'{x}{y}') # 분리사이 공백 표시 문자 , 숫자
print(x,y) 
print()

msg = 'kbdsaaaaaaaadssadsdsadsadx'
print('길이' , len(msg))
print('갯수', msg.count('a'))
print(msg[0:2])