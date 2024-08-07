def funcA():
    print("function A start")
    funcB()
    print("function A end")

def funcB():
    print("function B start")
    funcC()
    print("function B end")

def funcC():
    print("function C start")
    print("function C end")


if __name__ == "__main__":
    funcA()
