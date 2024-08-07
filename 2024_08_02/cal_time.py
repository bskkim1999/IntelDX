import time
import math


start=time.time()
a=math.factorial(1000000)
end=time.time()
print(a)
print("end-start : {}".format(end-start))