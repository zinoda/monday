# 06 test pickle.py

# open(1파일명, 모드w/rb, 인코딩)
# dump 쓰기 /load 읽기
# 피클로 파일처리 import 필요

import pickle
import time

fileName = 'C:/Mtest/move.pckl'
mybest = {'슈퍼맨superman' : 9.72 , '아이ironman' : 7.4 , '손흥민' : 5.3}

pickle.dump(mybest, open(fileName,'wb'))
print(fileName, '피클저장 성공했습니다')
print('_' * 60)
print()

time.sleep(1)
data = pickle.load(open(fileName , 'rb'))
print(data)
print(fileName, '피클읽기 성공했습니다')