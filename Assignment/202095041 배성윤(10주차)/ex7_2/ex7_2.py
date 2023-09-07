f=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_2/score.txt","r")
a=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_2/report.txt",'w')

while True:

    score=f.readline()

    if score == '':
        break
    scorelist=score.split()
    name=scorelist[0]
    
    m=0
    for i in range(1,4):
        
        m=m+int(scorelist[i])
    print(name+"의 총점 :{} ,평균:{}".format(m,m/3))
    print(name+"의 총점 :{} ,평균:{}".format(m,m/3),file=a) 
    
a.close
f.close
