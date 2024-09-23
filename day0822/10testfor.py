#10testfor.py

# 변수선언안하고 for 대표변수 처리

for k in range(1, 11 , 1) :
    print(k,end='') # print() 함수 자동 라인개행포함 엔터기능<br> ,end는 일렬  ,end='\t' 는 일렬공백
    # 5개씩 6줄 출력이니깐 if조건



print()
print()

for k in range(1 , 3000001 ,1 ) :
    print(k, end='\t')
    if k%5==0 :
            print()