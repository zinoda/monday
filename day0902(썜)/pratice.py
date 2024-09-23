# pratice .py

class book :
    def __init__(self,title,author,year) :
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self) :
        print(f"title : {self.title}")
        print(f"author : {self.author}")
        print(f"year : {self.year}")

my_book = book("나니아연대기" , "몰루" , 1980)

my_book.display_info()


class student :
    def __init__(self,name,age,grade) :
        self.name = name
        self.age = age
        self.grade = grade 
    
    def display_info(self) :
        print(f"학생 이름 : {self.name}")
        print(f"학생 나이 : {self.age}")
        print(f"학생 학년 : {self.grade}")

    
    def is_grade(self) :
        if self.grade >= 6 :
            print(f"{self.name} 은 졸업했습니다")
        else :
            print(f"{self.name}은 졸업하지 못했습니다")


student1 = student("하하호" , 14 , 8)
student2 = student("커커피" , 10 , 3)

print('-' *30)

student1.display_info() 
print()
student1.is_grade()

print()


student2.display_info()
print()
student2.is_grade()

print()