# 10 dict .py

mysite = {}
mydata = dict()

mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'
# print(mysite)  # 제일 단순 출력
print()

mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'

#for 반복문
for key in mysite : 
    print(key, ':' , mysite[key])