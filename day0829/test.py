#test.py



#문제 1  변수사용(name , age ,gender), 키보드입력., 나이는 숫자
#문제 2 나이 입력 범위 20~ 70 사이  / 조건 20미만 청소년 1~ 19 , 20 ~ 30 청년 31~65중년  66이상 노년
#문제 3  남자/남/man 입력 -> 남자출력   여자/여/woman입력 -> 여자
#문제 4


name = input('이름을 입력하세요 >>>>')

while True :
    age = int(input('나이를 입력하세요 >>>>'))
    if 20 <= age <= 70 :
        break
    else :
        print('나이는 20세 이상 70세 이하만 입력 가능합니다.')


if age < 20 :
    age_group = '청소년'
elif 20 <= age <= 30 :
    age_group = '청년'
elif 31 <= age <= 65 :
    age_group = '중년'
elif age >= 66 :
    age_group = '노년'


while True :
    try:
        gender = input('성별을 입력하세요 >>>>')
        if gender in ['남자' , '남' , 'man'] :
            gender = '남자'
            break
        elif gender in ['여자' , '여' , 'woman'] :
            gender = '여자'
            break
        else :
            print ('잘못된 성별 입니다. 다시 입력하세요')
    except ValueError :
        print('유효한 숫자를 입력하세요')

print('-' * 50) 



print(f'이름 : {name}')
print(f'나이 : {age}세 , {age_group}') 
print(f'성별 : {gender}')