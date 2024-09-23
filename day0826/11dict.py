# 11 dict .py

mysite = dict()


mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'


for i,k  in enumerate(mysite) :
    print(i , ' : ' , mysite[k])

print()


for k , v in mysite.items( ) :
    print(k, ':' , v)

print()


for a in mysite : 
    print(a, ':' , mysite[a])