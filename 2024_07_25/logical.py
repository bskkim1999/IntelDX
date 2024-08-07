logicValueOne=bool(input("first logic value input:") )
logicValueTwo=bool(input("second logic value input:") )

if logicValueOne == 'true':
    logicValueOne = True
elif logicValueOne == 'false':
    logicValueOne = False
else:
    print("Invalid input for the first logic value. Assuming False.")
    logicValueOne = False

if input_two == 'true':
    logicValueTwo = True
elif input_two == 'false':
    logicValueTwo = False
else:
    print("Invalid input for the second logic value. Assuming False.")
    logicValueTwo = False

print("logicalValueOne = {} not logicalValueOne = {}".format(logicValueOne, (not logicValueOne)))
print("{} and {} = {}".format(logicValueOne, logicValueTwo, (logicValueOne and logicValueTwo) ))
print("{} or {} = {}".format(logicValueOne, logicValueTwo, (logicValueOne or logicValueTwo) ))

#논리연산자는 논리값과 논리값을 연산해서 논리값을 리턴하는 연산자이다. 

