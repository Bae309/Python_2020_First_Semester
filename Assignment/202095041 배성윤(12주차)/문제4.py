num1=int(input("첫번째 정수 입력 : "))
num2=int(input("두번째 정수 입력 : "))
num3=int(input("세번째 정수 입력 : "))

if num1 >= num2 :
    if num1 >= num3:
        print("가장 큰 수는",num1,"입니다")
    else :
        print("가장 큰 수는",num3,"입니다")

else:
    if num2 >= num3:
        print("가장 큰 수는",num2,"입니다")
    else :
        print("가장 큰 수는",num3,"입니다")

    
