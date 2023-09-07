cal=int(input("원하는 연산번호를 입력하세요(덧셈 : 1, 뺄셈 : 2, 곱셈 : 3, 나눗셈 : 4) : "))
if cal < 1 or cal >4 :
    print("잘못 입력하셨습니다. 다시 시도해주세요.")

else:
    num1=int(input("첫번째 양의 숫자 입력 : "))
    num2=int(input("두번째 양의 숫자 입력 : "))

    if cal==1:
        print(num1,"+",num2,"=",num1+num2)

    elif cal==2:
        print(num1,"-",num2,"=",num1-num2)

    elif cal==3:
        print(num1,"*",num2,"=",num1*num2)
    
    else:
        if num2 >0:
            print(num1,"/",num2,"=",num1/num2)
        if num2==0:
            print("0으로 나눌수 없습니다")
             
