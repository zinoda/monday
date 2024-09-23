# 01 deftuple.py

def data_hap(x,y,z,a,b,c) :
    hap = 0
    hap = x+y+z+a+b+c
    return hap


def my_hap(*args) :
    print('*args타입' , type(args)) # *args타입 'tuple'
    hap = 0 #없으면 에러남
    for num in args :
        hap = hap + num
    return hap 

data = my_hap(6,11,24,7,5,21,39)
print('데이터 결과' , data)
total = data_hap(6,9,21,7,23,21)
print('계산처리 합계', total)
print('계산처리 합계', data_hap(6,9,21,7,23,21))









'''
print('x id' , id(x)) # 140717594262104 데이터를 기억하는 번지
    print('y id' , id(y)) # 140717594262104 데이터를 기억하는 번지
    print('z id' , id(z)) # 140717594262104 데이터를 기억하는 번지
    print('x타입' , type(x))
    print('y타입' , type(y))
    print('z타입' , type(z))
'''
