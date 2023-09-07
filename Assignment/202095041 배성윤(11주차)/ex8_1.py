def hap(x,y) :
    sum=0

    if x > y :
        temp=x
        x=y
        y=temp

    while x <= y :
        sum=sum+x
        x=x+1

    print()

    return sum

num1=int(input("첫번째 숫자 입력 : "))
num2=int(input("두번째 숫자 입력 : "))

sum=hap(num1,num2)

print("입력하신 정수 사이의 합은",sum,"입니다")
