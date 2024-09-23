# 02testlist.py

mylist = [ ] # 리스트 선언
mydict = { } # 딕트 선언

mylist.append('lee')
mylist.append(90)
mylist.append(85)
mylist.append(True)
mylist.insert(1, '빅데이터')
mylist.pop(3)
mylist.remove(90)

for k in mylist :
    print(k , end='\t')

print()

# 리스트 갯수 , count(데이터) , len()

cnt = mylist.count('lee')
print('리스트갯수' , cnt)