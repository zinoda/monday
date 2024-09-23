# 02split.py

url = 'www.google.com'
print(url)


myret = url.split('.') # 자동으로 리스트화 , 없는 문자 출력시 그냥 다 나옴
print(myret)
print(url.split(','))
print(list(url)) # 비권장
