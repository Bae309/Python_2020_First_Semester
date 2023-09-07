f=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_4/members.txt","r")
a=open("C:/Users/베성윤/Documents/Assignment/1학년 1학기/SW 프로그래밍사고/Assignment/202095041 배성윤(10주차)/ex7_4/report2.txt","w")

while True :

     score = f.readline()

     if score == "":
          break
     scorelist=score.split(',')
     name=scorelist[0]
     j=scorelist[1]
     c=scorelist[2]
     h=int(c)
     j=scorelist[1]
     if j.startswith("학"):
          b=15000*h
          print(name+":  등록금액 :",b)
          print(name+":  등록금액 :",b,file=a)
     if j.startswith("교"):
          b=30000*h
          print(name+":  등록금액 :",b)
          print(name+":  등록금액 :",b,file=a)
     if j.startswith("직"):
          b=30000*h
          print(name+":  등록금액 :",b)
          print(name+":  등록금액 :",b,file=a)
     if j.startswith("일"):
          b=50000*h
          print(name+":  등록금액 :",b)
          print(name+":  등록금액 :",b,file=a)

f.close()
a.close()
