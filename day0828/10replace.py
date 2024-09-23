#replace.py

#문자, 문자열변경 replace(변경대상,새로운대상)
#문자,문자열 공백제거 strip

msg = '            it is a best python       '
# for k in range(len(msg)) :
#     print(msg[k])

# for k in range(len(msg)) :
#     if msg[k] not in '' :
#         print(msg[k] , end= '')      위에 꺼 2개 할빠에 아랫꺼한다

print(msg.replace(' ', ''))


mylist = msg.split()
print(mylist)