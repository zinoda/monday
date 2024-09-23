# 03join.py

url = 'www.google.com'
print(url)


myret = url.split('.') # 자동으로 리스트화 , 없는 문자 출력시 그냥 다 나옴

ct =' ' # '공백' join 연결 하면 효과
print(ct.join(url))