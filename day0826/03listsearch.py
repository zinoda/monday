# 03listsearch.py

data = [7, 8, 9, 1, 2]

search = int(input('데이터찾기 >>> '))
if search in data :
    print(search, ' 검색 성공 ok')
    print('결과' , search in data)
else : 
    print('결과', search in data)
    print(search, '검색 성공 failed')


   
    
# 데이터있으면 성공메세지 데이터출력
# 데이터없으면 실패메세지
# 참고 ) for 대표변수 in range(5) :
# list에서 데이터 찾기 할때 in 키워드 사용

