#07 tuple.py

# 튜플 () 표시
# 튜플은 리스트와 비슷 , 수정이 불가함

pos = ('홍대' , 126.745 , 37.080, '홍대', 290.344)

# 튜플 for 반복문으로 출력
for k in range(len(pos)) :
    print(pos[k], end = '\t')


print()
print('-' *30)

for i,v in enumerate(pos) :
    print(i , ':' , v)
