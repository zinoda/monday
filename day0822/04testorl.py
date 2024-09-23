#04testcal.py

# 변수선언 및 초기화
a,b,c= 7,2,4
x,y,z = False, False, False # 0초기화보다는 False 권장


# 관계연산=비교연산  > < >= <= == !=
# 논리연산 and or not is in
x= ( (a >= b) and ( b >= c) ) 
y= ( (a >= b) or ( b >= c) )  
z= ( a != b ) 
print(x) #false
print(y) #true
print(z) #true



