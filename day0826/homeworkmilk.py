# homework milk.py

apart = [
    [101, 102 , 103 , 104] ,
    [201, 202 , 203 , 204] ,
    [301, 302 , 303 , 304] ,
    [401, 402 , 403 , 404]
]

unpaid = [101, 204 , 302 , 403]


for a in apart :
    for b in a :
        if b in unpaid :
            print(f"{b} : 우유배달 x")
        else :
            print(f"{b} : 우유배달 o")

            
   
#힌트 중첩문  for 사용
# for a in ~
    #for b ~~
        # if 조건 in unpaid
            # 우유배달 x
        # else :
            # 우유배달 o


#101호 우유 배달 중지x
#102호 우유 배달 계속o
#103호 우유 배달 계속o
#104호 우유 배달 계속o

#201호 우유 배달 계속o
#202호 우유 배달 계속o
#203호 우유 배달 계속o
#204호 우유 배달 중지x

#301호 우유 배달 계속o
#302호 우유 배달 중지x
#303호 우유 배달 계속o
#304호 우유 배달 계속o

#401호 우유 배달 계속o
#402호 우유 배달 계속o
#403호 우유 배달 중지x
#404호 우유 배달 계속o