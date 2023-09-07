num1=int(input("첫번째 숫자 입력 : "))
op=input("연산자 입력(+,-,*,/) : ")
num2=int(input("두번째 숫자 입력 : "))

if (op == "+") :
     print("수식결과",num1,op,num2,"=",num1+num2)

if (op == "-") :
     print("수식결과",num1,op,num2,"=",num1-num2)

if (op == "*") :
     print("수식결과",num1,op,num2,"=",num1*num2)

if (op == "/") :
     print("수식결과",num1,op,num2,"=",num1/num2)

else :
     print("해당되는 연산자가 없습니다")
