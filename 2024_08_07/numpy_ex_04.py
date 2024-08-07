import numpy as np

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
twoDim = np.array( [ [1,2,3], [4,5,6], [7,8,9] ] )

A = np.array([1,2,3,4])
B = np.array([5,6,7,8])

result1 = arr1+arr2		# 넘파이 배열에 + 연산이 적용된다. 
result2 = A+B
result3 = A<3

print(result1)
print(result2)
print(result3)
print(twoDim)
print(twoDim[0][0])
print(twoDim[0][1])
print(twoDim[0][2])
