#01testlist.py

data = [ # 3행 * 4열
        [70,71,72,73,74] ,
        [75,76,77] ,
        [80,81,82,83,84]
    ]       

for k in range(len(data)) : #행
    for b in range(len(data[k])): # 열갯수
        print(data[k][b], end = '\t')
    print()





# 힌트 중첩 for 반복문 권장 , while 반복문 비권장
# range(len()) 이용하면 편함
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# for a in range(0,3,1) : #3행
#      for b in range(0,4,1) :
#         print(data[a][b], end = '\t')
# print()
 
