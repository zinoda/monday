# home work dict. py

score_dict = {
    '김자바' : [100,60] ,
    '이합격' : [90,77] ,
    'kang' : [82,34] ,
    'park' : [90,34]
    }

list_kor = []
list_eng = []

for scores in score_dict.values() :
    list_kor.append(scores[0])
    list_eng.append(scores[1])

for student , scores in score_dict.items() :
    total_scores = sum(scores)
    average_scores = total_scores / len(scores)

    print(f" {student}  총점  {total_scores}  평균  {average_scores:.0f}")

# 아래처럼 출력
# 김자바 총점 160 평균 80
# 이합격 총점 167 평균 83
# kang  총점 116 평균 58
# park 총점 124 평균 62

