# member = ['박찬호', '박지성', '박세리']

# print(member[0])
# print(member[1])
# print(member[2])

# member.append('박혁거세')
# print(member)
# print(len(member))

# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# i=0
# for item in balls:
#     print("balls[{}] = {}".format(i, item))
#     i = i+1
    
    
# print("=================================")

# for index, item in enumerate(balls):
#     print('balls[{}] = {}'.format(index, item))
    
# print(balls.index('야구공'))

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return int(self.value)  # 반드시 정수를 반환해야 함

# 슬라이싱에서 사용하기
numbers = [10, 20, 30, 40, 50]
obj = MyNumber(2.9)
tmp = obj.__index__()
#print(tmp)
#print(int(2.9))
print(numbers[tmp:tmp+2])  # [30, 40]