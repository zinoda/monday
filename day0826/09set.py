# 09 set. py

# 셋 set { }
# 순서 x , 중복 x
# append() , insert() == add() 대체
# 전체삭제 clear()
wish = {'대저' , 126.745 , 37.080, '대저', 37.080, 126.159, '대저'}

wish = { } # 선언하면 set 아니라 dict로 인식함 / 실행하면 에러남
wish.add('엘지')
wish.add('kt')
wish.add('엘지')
wish.add(37.081)
print(wish)
print()