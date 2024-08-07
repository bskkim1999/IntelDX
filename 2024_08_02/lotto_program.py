import random

#global
lotto_number=[]
count=0

def save_lotto_number(num):
    #번호저장
        global lotto_number
        lotto_number=[]  #초기화
        
        for a in range(0,num,1):
            lotto_number.append(random.randrange(1,46))  #1 ~ 45
    
        print("def", lotto_number)

while True:
    num=int(input("번호개수를 입력해라 : (1 ~ 6)"))
    
    if num>=1 and num<=6:
        save_lotto_number(num)
        
        
        
        #번호가 중복하는지 검사
        while True:
            count=0
            print("calculate...")
            
            #오름차순으로 정렬
            lotto_number.sort(reverse=False)
                
            #중복검사
            for i in range(1,num,1):
                if lotto_number[i] - lotto_number[i-1] == 0:
                    count = count + 1
                
                else:
                    continue
            
            
                
            #번호가 중복한다면?
            if count > 0 :
                save_lotto_number(num)  #다시 저장
                
                    
                    
            #번호가 중복하지 않는다면?
            else:
                
                print(lotto_number)
                exit()  #program exit
        

        
        
    else:
        print("다시 입력해라")
        continue
    
    

