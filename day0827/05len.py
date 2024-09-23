#05len.py

jumin='970722-1234567'
jumin1='970722' # 앞번호 6자릿수
jumin2='1234567' # 뒷번호 7자릿수

# 문제 총자릿수 6 - 7 = 14자릿수
# 문제 총자릿수 6 7 = 13자릿수
# 문제 총자릿수 jumin1 6자릿수 jumin 2 7자릿수  lne() 사용 변수 받아서

frontlen = len(jumin1)
backlen = len(jumin2)

if (frontlen != 6) and (backlen != 7 ) :
    print('다시 정확한 데이터를 입력하세요')
else :
    print('정확한 데이터 감사합니다')