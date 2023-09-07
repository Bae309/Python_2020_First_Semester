subject=1
total=0


while subject <=10:

    num=int(input(str(subject)+"번째 숫자 입력 : "))
    subject=subject+1
    
    while (subject % 2 == 0):
        num =-num
        total=total+subject
        print(subject,"번째 숫자",num)
        subject=subject+1

else :
    print("총합 : ", total)
        
    
