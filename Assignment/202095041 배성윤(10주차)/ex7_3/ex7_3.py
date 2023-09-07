score=[]

f=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_3/score1.txt","r")

for i in range(4):
    score.append(f.readline().split())

for i in range(4):
    score[i][1]=float(score[i][1])

    if score[i][1]>=90:
        score[i].append("A")

    elif score[i][1]>=80 and score[i][1]<90:
        score[i].append("B")

    elif score[i][1]>=70 and score[i][1]<80:
        score[i].append("C")

    elif score[i][1]>=60 and score[i][1]<70:
        score[i].append("D")

    else:
        score[i].append("E")

for i in range(4):
    print("{}{:>3}".format(score[i][0],score[i][2]))

with open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_3/report2.txt","w") as f1:
    for i in range(4):
        print("{}{:>3}".format(score[i][0],score[i][2]),file=f1)
        

