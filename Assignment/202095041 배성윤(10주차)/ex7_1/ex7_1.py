import random

#f=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/num.txt","w")
with open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/num.txt","w") as f :
    for i in range(5):
        for j in range(5):
            f.write(str(random.randint(1,100)))
            f.write(' ')
        f.write("\n")

with open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/num.txt","r") as f :
    with open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/avg.txt","w") as f1 :
        
        j=0
        while True :
            j=j+1
            score=f.readline()
            if score==' ':
                break
            scorelist=score.split()

            total=0

            for i in range(5):
                total=total+int(scorelist[i])

            print(j,"번쨰 학생의 평균: ", total/5)
            print(j,"번쨰 학생의 평균: ", total/5,file=f1)
