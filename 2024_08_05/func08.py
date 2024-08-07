def addFunction(num):
    if num>0:
        print("num=",num)
        addFunction(num-1)
        #print("num=", num)


if __name__=="__main__":
    addFunction(10)
    print(__name__)
