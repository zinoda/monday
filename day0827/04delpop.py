# 04 delpop.py
import time


# remove , del , pop 제거 삭제 기능
# remove(데이터 값) /  pop (위치) / del 대상[위치]
# clear  전부삭제

# append()  , insert (위치, 값) , add () 추가 기능
#  추가 dict이름[k] = datavalue
#  똑같은 이름이면 덮어씌어지면서 추가 됨


data = [7,8,9,10,3,5,2,4,1]
data.remove(9) # 9삭제
data.pop() # 2 삭제
print(data) # [ 7,8,10,3,5,2,4]

del data[2]# [7,8,3,5,2,4]
print(data)
time.sleep(1)

del data[1:4] # 구간삭제 
print(data)

time.sleep(0.5)
data = [7,8,9,10,3,5,2,4,1]
data.clear()
print(data)
print('삭제연습끝 드디어 dict 실습 ')

#count(인자) , len(데이터) 
#count(90) , len(리스트/딕트/문자열) 
