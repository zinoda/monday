# 01testlambda.py
# 람다식은 import 기술 안함 , 키워드 lambda 기술

def mycal(su) :
    cal = 3 * su+8
    return cal



print('일반식' , mycal(5))
my1 = lambda su : 3*su+8
print('람다식' , my1(5))
print('람다식' , (lambda su : 3*su+8)(5))
print()

def myAdd(x,y) :
    return x+y

print('일반식' , myAdd(3,4))
my2 = lambda x,y : x+y
print('람다식' , my2(3,4) )
print('람다식' , (lambda x,y : x+y)(3,4) )
print()

#함수에서 계산처리후 if~else 제어문 리턴값

def mycheck(su) :
    if su %2 == 0 :
        print('짝수')
    else :
        print('홀수')

print(mycheck(17))
print('람다식' , (lambda su : '짝수' if su%2 == 0 else '홀수')(17))




print()