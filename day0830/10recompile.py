# 09resub.py
import re


# 정규  sub(1,2,3)

data = '''
kim 840916-1094852
lee 921207-2059326
goo 981024-1674938
'''

# compile('\d{6}-\d{7}') 적용후 sub()확인
# 문자열함수 for~if data [시작위치] 
# 정규식 sub / re.sub('-[0-9]{4}-' , '-****-' , phone)

# \n 라인 개행 enter 기능 \t 탭 \b 백space  

com = re.compile('-\d+')
first = com.sub('-*******',data)
print(first) #비권장
print()

two = re.sub('[0-9]{7}','*******',data)  #추천 
print(two) 