# 05ospath.py

# x임포트문장 필요없슴 import file ~~~
# pathname = '경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
#ff=open(1,2,3) 대체 with open(1,2,3) as ff
import sys
import os.path


file = 'C:/Mtest/kakao.txt'
save_path = os.path.abspath('C:/Mtest/kakao.txt')
try :
    if not os.path.exists(save_path) :
        print(save_path, '대상 파일이 존재하지 않습니다')
        #sys.exit()
    else :
        pass
except Exception as EX :
    print('에러이유 확인' , EX)







