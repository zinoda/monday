# 07comprehension.py [ 연산  if/else for~~]

message =[ 'spam','ham' , 'spam', 'ham', 'spam','spam']

# 문제 1  for ~ if 제어
# spam출력. 갯수출력

for k in message :
    if k == 'spam' :
        print(k, end= ' ')

print()
print()

# 문제 2 [ 만앞 if else  불뒤 for ~~~~] comprehension처리
# 문제 2 [ 만앞 for ~~~~] comprehension처리 
temp_list = [k for k in message if 'spam' in k]
print(temp_list)



print()
dummy = []
# 문제 3 ) spam = 0 han=1 dummy = [0,1,0,1,0,0] ret = []
# message= [ 'spam','ham' , 'spam', 'ham', 'spam','spam']
for k in message :
    if k == 'spam' :
        dummy.append(1)
    else :
        dummy.append(0)

print(dummy)

mydummy = [0 if k=='spam' else 1 for k in message]
print('comprehension' , mydummy)