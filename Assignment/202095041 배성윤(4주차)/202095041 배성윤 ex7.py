i=1
while i<=29:
    print("=",end="")
    i=i+1
print()
month=int(input("가장 좋아하는 월은?(종료 : 0) : "))
while i<=29:
    print("=",end="")
    i=i+1
print()
   

while True:

    if ((month < 1) or (month > 12)) :
        break

    elif ((month >=3) and (month <=5)) :
        print("******",month,"월 ******")
        print(month,"월은 봄에 해당됩니다.")
        break

    elif((month >=6) and (month <=8)) :
         print("******",month,"월 ******")
         print(month,"월은 여름에 해당됩니다.")
         break

    elif((month >=9) and (month <=11)) :
         print("******",month,"월 ******")
         print(month,"월은 가을에 해당됩니다.")
         break

    else :
        print("******",month,"월 ******")
        print(month,"월은 겨울에 해당됩니다.")
        break
        
