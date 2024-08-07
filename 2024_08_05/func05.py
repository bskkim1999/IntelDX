import time


def greet(name):
    print("{}씨 안녕하세요.".format(name))


#Main
while True: 
    greet("홍길동")
    time.sleep(0.5)
    greet("박찬호")
    time.sleep(0.5)
    greet("신유빈")
    time.sleep(0.5)


