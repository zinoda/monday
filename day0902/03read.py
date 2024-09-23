# 12file.py

# x임포트문장 필요없슴 import file ~~~
# pathname = '경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
#ff=open(1,2,3) 대체 with open(1,2,3) as ff
import time


#파일읽기 처리 read() 대신 readline() 한라인씩 읽기
pathName = 'C:/Mtest/sample.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
data = rfile.readline()
# 주석 data = rfile.readline()
print(data)
print('-' * 50)
rfile.close()
time.sleep(0.5)
print(pathName,'파일저장성공했습니다')
print()



time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
    #my = myfile.read() 전체
    my = myfile.readline() #한줄씩처리
    while my != '' : 
        print(my)
        my = myfile.readline()


time.sleep(0.5)
print(fileName, '파일저장성공했습니다')
print()





