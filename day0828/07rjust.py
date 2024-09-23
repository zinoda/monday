# 07rjust.py

for a in range(1,6,1) :
    pass
   # print(f'{a} * {a} = {a*a}')
   # print(a , '*' , a, '=' , (a*a))

print( )

for a in range(1,6,1) :
   # print(a , '*', a , '=' , str(a*a))
    print(a , '*', a , '=' , str(a*a).rjust(3))


for a in range(1,6,1) :
   # print(a , '*', a , '=' , str(a*a))
    print(a , '*', a , '=' , str(a*a).rjust(3))