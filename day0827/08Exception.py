


x,y = 0,0
hap , gob , mok , nmg = 0, 0, 0, 0

hap = x+y ; mok = x/y 
nmg = x%y ; gob = x*y

x = int(input('x정수입력(0숫자제외) >>>>'))
y = int(input('y정수입력(0숫자제외) >>>>'))

try :
    x = int(input('x정수입력(0숫자제외) >>>>'))
    y = int(input('y정수입력(0숫자제외) >>>>'))

    
    print(f'{x} + {y} = {hap}')
    print(f'{x} / {y} = {mok}')
    print(f'{x} % {y} = {nmg}')
    print(f'{x} * {y} = {gob}')
except :
    pass






print('쇼핑목록')
print('주차처리')
print('정산성공')