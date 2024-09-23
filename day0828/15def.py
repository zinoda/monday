# 15def return.py

# 파이썬에서 함수 정의 시작 키워드 def 함수 이름 ( ) :
# 사용자정의 함수 매개인자 구구단실습확인
# 사용자정의 함수에서 처리 후 외부에 값을 줄 때 return 값을 준다
# 사용자정의 함수 매개인자 + 리턴값

def book ( ) :
    title = '몽블랑' #지역변수 = local variable = 휘발성
    return title
def pay ( ) :
    m = 7800 # 지역변수 = local variable=휘발성
    return m



def main ( ) :
    print("main함수")
    # print("책제목" , title)  에러 발생
    # print("책가격" , m)
    data = book()
    value = pay()
    print('책제목' , data)
    print('책가격' , value)
    print('책가격' , book())
    print('책가격' , pay())

if __name__ == '__main__' :
    main( )