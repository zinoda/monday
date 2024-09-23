score_dict = {
    '김자바' : [100,60] ,
    '이합격' : [90,77] ,
    'kang' : [82,34] ,
    'park' : [90,34]
    }

list_kor = []
list_eng = []


for score in score_dict.values( ) :
    list_kor.append([0])
    list_eng.append([1])

for a , b in score_dict.items ( ) :
    total_score = sum(b)
    average_score = total_score / len(b)

    print(f"{a}  총점  {total_score}  평균  {average_score:.0f}" )
