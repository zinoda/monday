# 09resub.py
import re


phone = '010-7800-1234 박이썬'
# 힌트 re.sub('1패턴' , '2변경적용' , phone)
model = re.sub('-[0-9]{4}-' ,'-****-' , phone)

print(phone)
print(model)
# msg = 'my best &%(@ 245 오렌지 is (_^# 수박 cherry as tea'

# result1 = re.findall('[\w]+' , msg)
# result2 = re.findall('[\W]+' , msg)
# result3 = re.findall('[a-zA-Z0-9가-힣]+', msg)
# result4 = re.findall('[a-zA-Z0-9가-힣]+', msg)


# print(result1) ; print()
# print(result2) ; print()
# print(result3) ; print()
# print(result4) ; print()
