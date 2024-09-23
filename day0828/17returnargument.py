# 17 return argument. py

def book() :  # 매개인자 x , 리턴값 o
    title = '몽블랑'
    return title

def pay() :  # 매개인자 x , 리턴값 o 
    m = 7800
    return m

def mycal(x,y,z) :  #매개인자 o , 리턴값 o
    total = x+y+z
    avg = total//3
    return avg # 3개 데이터를 받아서 계산연산 처리 후 최종값을 리턴하겠다

# mycal 함수호출
#mycal 함수 리턴값이 있으면 변수 = 함수이름 / mycal함수 리턴값이 있으면 print(함수이름())
data = mycal(70,85,64)  
print('mycal함수 호출 성공' , data)

# def gugudan(name,dan) : # 매개인자 o , 리턴값 x
#     pass

# def blue ( ):  # 매개인자 x , 리턴값 x
#     color = 'dark'

# def main () :
#     print("main함수")