# 01test.py

mylist = [ ] # 리스트 선언
mydict = { } # 딕트 선언

mylist.append('lee')
mylist.append(90)

print('-' * 50)
for k in mylist :
    print(k , end='\t')

print()

mydict[500] = '차박'
mydict[700] = '등산'
mydict[300] = '여행'
# print(mydict) # 비권장

for k ,v in  mydict.items() :
    print(k, ':' , v)

print()

for i , k in  enumerate(mydict) :
    print((i+1),' ',k , mydict[k])


