# # 초기 영화 목록
# movie_rank = ["닥터스트레인지", "스프릿", "럭키"]

# # 새로운 영화 추가
# movie_rank.append("배트맨")

# # 수정 전 영화 목록 출력
# print("수정 전 영화 목록:")
# print(movie_rank)

# print("=================")

# # 영화 제목이 "스프릿"인 경우 "슈퍼맨"으로 변경
# for i in range(len(movie_rank)):
#     if movie_rank[i] == "스프릿":
#         movie_rank[i] = "슈퍼맨"

# # 수정 후 영화 목록 출력
# print("수정 후 영화 목록:")
# print(movie_rank)


# list1 = ["c", "cpp", "java"]
# list2 = ["python", "go", "c#"]

# print(list1)
# print(list2)


# merged_list = list1 + list2

# print("====")
# print(merged_list)  

import random


rand_num=[]
sum=0
aver=0

for i in range(0,10,1):
    rand_num.append(random.randrange(1, 101))
    
    
print(rand_num)

#오름차순
rand_num.sort()

print(rand_num)


print("가장 작은 수 : {}".format(rand_num[0]))
print("가장 큰 수 : {}".format(rand_num[9]))

for i in range(0,10,1):
    sum = sum + rand_num[i]
    
aver = sum / 10.0

print("합계 : ", sum)
print("평균 : ", aver)


