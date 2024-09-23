#10testfor.py

# for 대표변수 처리
# 반복 - for,while
# 반복에서 보조제어문 break -> 반복탈출 , continue 복귀
for k in range(1, 11,) :
    if k==5 :
        continue
    print(k, end='  ')
    # 1 2 3 4 6 7 8 9 10 (5뺴고 출력됨)


  