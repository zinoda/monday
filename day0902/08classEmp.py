# 13classEmp.py

class Emp:
    user_id = '아이디' #전역변수=global variable = member변수
    user_pwd = '1234'

    def __init__(self,id,pwd) :
        self.user_pwd = id
        self.user_id = pwd


    def insert(self,age):
        print('전역변수 user_id' , self.user_id)
        print('전역변수 user_pwd',self.user_pwd)
        print('전달된 나이' , age)
        print('insert into처리\n')


    def delete(self):
        print('삭제처리')
        print('딕트del, delete where 조건')
        

ob = Emp('sky' , '7789')
ob.insert(7)
ob.delete()





print()