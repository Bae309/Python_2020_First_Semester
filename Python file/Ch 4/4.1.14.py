sex=input("당신의 성별은('M or m' 또는 'F or f') :")
height=float(input("키를 입력(cm) : "))/100
weight=float(input("몸무게 입력(kg) : "))

if (sex=='M' or sex=='m') :
     avg=height*height*22

     if 110<=weight/avg*100<=119 :
          print("과체중")
     elif weight /avg*100>=120 :
          print("비만체중")
     else :
          print("표준체중")

elif (sex=='F' or sex=='f') :
     avg=height*height*21

     if 110<=weight/avg*100<=119 :
          print("과체중")
     elif weight /avg*100>=120 :
          print("비만체중")
     else :
          print("표준체중")

else :
     print("성별입력이 잘못되었습니다")
