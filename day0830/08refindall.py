# 08refindall.py
import re

msg = 'my best &%(@ 245 오렌지 is (_^# 수박 cherry as tea'

result1 = re.findall('[\w]+' , msg)
result2 = re.findall('[\W]+' , msg)
result3 = re.findall('[a-zA-Z0-9가-힣]+', msg)
result4 = re.findall('[a-zA-Z0-9가-힣]+', msg)


print(result1) ; print()
print(result2) ; print()
print(result3) ; print()
print(result4) ; print()
