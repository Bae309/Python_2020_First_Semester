num1=int(input("첫번째 숫자 : "))
num2=int(input("두번째 숫자 : "))

if num1 > num2 :
    if num1%2==0:
        print("둘 중 큰 숫자는",num1,"이고, 짝수입니다")
    else:
        print("둘 중 큰 숫자는",num1,"이고, 홀수입니다")

if num2 > num1 :
    if num2%2==0:
        print("둘 중 큰 숫자는",num2,"이고, 짝수입니다")
    else:
        print("둘 중 큰 숫자는",num2,"이고, 홀수입니다")

