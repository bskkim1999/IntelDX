
def calculator(num1, num2):
    result1=num1+num2
    result2=num1-num2
    result3=num1*num2
    result4=num1/num2

    return (result1, result2, result3, result4)

inputNumber1=int(input("첫번째정수입력"))
inputNumber2=int(input("두번째정수입력"))

print("================")

result=calculator(inputNumber1, inputNumber2)
print(type(result))
print("사칙연산결과:", result)
print("plus : ", result[0])
print("minus : ", result[1])
print("multiply : ", result[2])
print("divide : ", result[3])

