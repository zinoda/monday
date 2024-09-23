#17listfor.py
import time

mylist = [ 'tea' , 78 ] 
print(mylist)

mylist.append('파이썬')
print(mylist)

mylist.append(23)
print(mylist)

mylist.insert(1, 'blue')
print(mylist)
print('-' * 50 )

mylist[0] = 'kakao'
print(mylist)

mylist[1] = 'naver'
print(mylist)

mylist.pop(0)
print(mylist)

mylist.remove('파이썬')
print(mylist)

mylist.reverse()
print(mylist)

mylist.remove('naver')
print(mylist)

mylist.sort()
print(mylist)

del mylist[1]
print(mylist)




# append('') -> 추가 /  insert (위치 , '') -> 추가  / [위치] -> 변경 / pop , remove , del -> 삭제
# 주의사항 ) sort() 적용은 같은 타입만 가능


print()
print()
# for  반복문 연습 1 2 3 4 5 6 7 8 9 10 
# su = 0
# for k in range(10) :
#         su = su + 1
#         print(su , end = ' ')
