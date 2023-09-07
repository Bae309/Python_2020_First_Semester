num=1
total=0

while num <=10 :

    score=int(input(str(num)+" 번째 숫자 입력 : "))

    if(score >=0) :
        total=total+score
        print(num,"번째 숫자 :",score)
        num=num+1
    else :
        break

else :
    print("총합 :",total)
    print("총평균 :",total/10)
