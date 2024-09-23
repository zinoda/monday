#09dictreturn.py

#함수의 리턴값 1개이상처리
#함수의 매개인자 1개이상처리 (*args)


def score_procedure(score_dict) :
    kor_list=[]
    eng_list=[]

    for data in score_dict.values() :
        kor_list.append(data[0])
        eng_list.append(data[1])
    
    kor_hap = sum(kor_list)
    eng_hap = sum(eng_list)
    kor_avg = kor_hap //len(kor_list)
    eng_avg = eng_hap //len(eng_list)
    return kor_hap , eng_hap , kor_avg , eng_avg

score = {
    'kim' : [100,60], 
    'lee' : [90,77],
    'goo' : [82,34]
}

a,b,c,d = score_procedure(score)

print('국어총점' , a)
print('영어총점', b)
print('국어평균', c)
print('영어평균', d)