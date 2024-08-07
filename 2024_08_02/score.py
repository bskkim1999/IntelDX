import statistics


scores=[]
hap=0
count=0

for i in range(0,10,1):
    scores.append(int(input("{}번 학생 점수입력:".format(i+1))))
    hap = hap + scores[i]
    
avg=hap/len(scores)

maxScore=max(scores)
minScore=min(scores)

for i in range(0,10,1):
    print("{}번 점수입력:".format(i))
    

for i in range(0,10,1):
    print("{}번 점수 : {}".format(i+1,scores[i]))
    
print("====")
print("성적합 : ", hap)
print("성적평균 : ", avg)
print("최대점수:", maxScore)
print("최소점수:", minScore)

print("특정 점수 이상의 학생 수 출력하기")
score = int(input("기준점수입력:"))

for i in range(0,10,1):
    if scores[i] >= score:
        count = count+1
    
    else:
        continue
    
print("해당하는 학생 수 : {}".format(count))
print(id(scores))

