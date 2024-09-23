#03play.py
import time
import game #물리적인 파일이름만 명시



print('03play.py')
time.sleep(0.5)

print(game.user_id)
print(game.user_pwd)

time.sleep(0.5)
game.terran()

time.sleep(0.5)
game.LG('그램')
miter = game.running()
print('코스길이' , miter)
print('코스길이' , game.running())

# game.py 문서
# 전역변수 user_id , user_pwd
# 함수 terran() , LG(lg) running()리턴값있음