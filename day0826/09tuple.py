# 09 tuple. py

t = (30, 20, 10, 50, 63, 7, 7, 67, 63, 20, 30, 63)
# print('갯수' , t.count(10))
# print('색인' , t.index(30))

print(t)
print()

mylist = list(t)
print(mylist)
mylist.append(7)
mylist.insert(2,63)
mylist.remove(20)
print(mylist)
print()
# 에러 t.append(7)
# 에러 t.insert(2,63)
# 에러 t.remove(20)
print()