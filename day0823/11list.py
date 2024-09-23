# 10list.py
import time

#lista.sort()

#lista.(reverse(true))

lista = [ 20, 10, 40 , 50, 30]
print(lista)
time.sleep(1)

lista.insert(2,9)  # 2번쨰에 '9'를 추가할거야
time.sleep(1)
print(lista)

lista.append(7)   # 맨 끝에 '7'를 추가할거야
time.sleep(1)
print(lista)

lista.pop(3)
print(lista)

lista.reverse()
print(lista)

print()