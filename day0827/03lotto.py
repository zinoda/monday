# 03lotto.py



lotto=[ 23, 19 , 5 , 42 ,19 , 27 , 23 , 5 ,23]
myset = set(lotto) #filtering
print(myset)
lotto = list(myset)
lotto.sort() #  오름차순
print(lotto)
print()

mylength = len(lotto)
if mylength < 6 :
    print('항목 하나 추가하셔야 처리 가능합니당')
elif mylength > 6 :
    print('항목 데이터 초과 되었습니다\n다시 확인하세요') 
elif mylength == 6 :
    print('데이터항목 정상입니다')


# 문제 ) lotto 갯수 6개 아니면 추가



# lotto.sort()
# print(lotto)
# 조건 1 ) 숫자 6개
# 조건 2 ) 중복숫자 제거
# 조건 3 ) 정수숫자로만 구성 되어야함
