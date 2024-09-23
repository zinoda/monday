# 09dictmenu.py
import time
import sys #프로그램 종료 sys.exit()

menu = dict()
flag = True
num , su , sel = 0,0,0
msg , info , message = '안내문','안내문','안내문'


while flag :
    pass
    print()
    num=int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료 >>>>'))
    if num == 9 :
        print('딕트처리를 종료합니다')
        flag = False
        sys.exit

    elif num == 1 : #딕트등록 mysite[200 키] = ' kakao'
        name = input('메뉴입력(key값)>>>') 
        price = input('가격입력(value) >>>')
        menu[name] = price
        print(name, '등록 성공했습니다')

    elif num == 2 : #딕트 전체 출력
       for i , k in enumerate(menu) :
        print(i,k,' ', menu[k])
        print()
       
    elif num == 3 : #딕트 수정 처리  #'key조회후 키값이 있으면 수정 get() 함수'
        name = input('기존 메뉴 이름 입력 >>>')
        if menu.get(name) == None :
            print('수정대상 데이터가 없습니다')
        else :
            rename = input('새로운 메뉴 이름 입력 >>>')
            reprice = input('새로운 가격  >>>') 
            menu.pop(name)
            menu[rename] = reprice
            print(rename, '등록이 변경 되었습니다')

        
    elif num == 4 :
        name = input('삭제대상 menu(키)값 입력 >>>')
        if menu.get(name) == None :
         print('삭제대상 딕트가 key 없습니다')
        else :
            menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
            
    elif num == 5 :
        name = input('조회 할 키 값 입력 >>>')
        if name in menu :
            print(f'{name} : {menu[name]}')
        else :
            print('조회 할 key 값이 없습니다')
    else :
        pass
        print('처리번호를 잘못 입력하셨습니다')


print()
# 사용자정의 함수
# 클래스
# 파일처리 - 파일저장 , 파일열기
# 예외처리
# crud
# ㄴ C  추가신규등록 create(insert=add)
# ㄴ R  READ 읽기
# ㄴ U  update 수정
# ㄴ D  delete 삭제

# mysite = dict() 
# mysite[100] = 'naver'
# mysite[200] = 'kakako'
# mysite[300] = 'apple'
# # for i,k in enmuerate(mysite) :
#     #print(i,k ,'' , mysite[k])

# mysite.items() 
# print(mysite)

# print()

# mysite[100] = '에이콘'

# for k,v in mysite.items() :
#     print(k, '' , v)

# print(mysite[200]) # 키 값 확인
# print(mysite.get(210)) #에러대신 None
