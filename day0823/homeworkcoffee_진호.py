# homeworkcoffee.py

money , sel = 0 , 9

money = int(input('금액 입력 >>> '))
while True :
    print('----------------------- 커피머신 -----------------------')
    data = int(input(' 1.커피(250) 2.코코아(200) 3.반환 9:종료>>> '))
    sel = int(data)
    print()
    if sel == 9 :
        break
    elif sel == 1 :
        if money >=250 :
            print('커피 주문 완료' , end= '   남은 잔액은 {}원입니다.'.format(money-250))
            break
        
        elif money < 250 :
            print('잔액이 부족합니다.')
            break
    elif sel == 2 :
        if money >= 200 :
            print('코코아 주문 완료' ,end = '  남은 잔액은 {}원입니다.'.format(money-200))
            break
        elif money < 200 :
            print('잔액이 부족합니다.')
            break

    elif sel == 3 :
        print('반환되었습니다')
        break
    else :
        print('입력이 잘못 되었습니다')



#if ~ elif ~ if 제어문으로 커피값 계산 
    


