level=int(input("직급을 입력 : "))
age=int(input("나이를 입력 : "))

if ((level == 7) or (level ==8)) and ((40 <= age) and (age <= 49)) :
     print("연금 80% 대상자입니다")

elif (((level == 5) or (level ==6)) and ((50 <= age) and (age <= 59))) :
     print("연금 100% 대상자입니다")

else : print("연금 대상자가 아닙니다")
