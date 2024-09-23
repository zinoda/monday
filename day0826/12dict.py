# 12 dict .py

mysite = dict()


mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.daum.kr' # 수정 편집
mysite['google'] = 'www,google.org'


# for key in mysite :
#     print(key, ':' , mysite[key])

# print()

# print(mysite.keys()) #키값목록

# print()
# print(mysite.values()) #벨류 값목록

print()
print(mysite['naver'])

print()

# print(mysite['navr'])  # 키 값 잘못 기술 , 키 값 없으면 에러 남
print(mysite.get('navr'))  # 키 값 잘못 기술 ,  키 값 없으면  none

print(mysite.get('naver'))


# 키 값 있어야 딕트 이름[키값] 출력 및 수정 , 신규등록이 가능하다.

mya = 'naver'  in mysite
myb = 'navr'  in mysite
print(mya) # true
print(myb) # false