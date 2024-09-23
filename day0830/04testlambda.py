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
    msg = '안내문'
    if su %2 == 0 :
        msg = '짝수'
    else :
        msg = '홀수'
        return msg

print('일반식', mycheck(17))
print('람다식' , (lambda su : '짝수' if su%2 == 0 else '홀수')(17))




print()

# 문제 1) 리스트 1 ~10 까지 출력 for,while  사용금지
data =list(range(1,11,1)) # 출력 [1 ~10]
print(data)

my =map((lambda su : su*su),data) #<map object at 0x000002805F6052D0>
print(list(my))

my =list(map((lambda su : su*su),data))
print(my)