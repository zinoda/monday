# 01 deftuple.py




def my_hap(*args) :
    print('*args타입' , type(args)) # *args타입 'tuple'
    hap = 0 #없으면 에러남
    for num in args :
        hap = hap + num
    return hap 


mylist = [6,11,24,7]  #수정 o , 쉽게 데이터 추가
mytuple =(5,10,23,6)  #수정 x,  쉽게 데이터 추가 x
mylist[1] = 54
print(mylist)

mytuple[1] = 94
print(mytuple)


