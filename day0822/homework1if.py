# homework1if.py

su = -78
message ='안내문'
#정수 = int = integer
#음수 0제로 양수 

#문제해결 su데이터값 음수,제로0,양수 인지 
#if~elif~elif~else
#if~elif~else

if su > 0 :
    message = '양수 데이터입니다'
elif su < 0 :
    message = '음수 데이터입니다'
else :
    message = '제로 데이터입니다'

print(su,message)

if su < 0 :
    print(su, '음수 데이터입니다')
elif su == 0 :
    print(su, '제로 데이터입니다')
elif su > 0 :
    print(su, '양수 데이터 입니다')
