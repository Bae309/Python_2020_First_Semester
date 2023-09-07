def isPrime(num) :
    
    if num in {2,3}:
        return True
    elif num%2==0 or num ==1:
        return False
    else:
        for i in range(3,num+1):
            if num %i==0:
                return False

def judge(number):
    while number != -1:
        if isPrime(number)== True:
            print("%d는(은) 소수입니다"%number)
            break
        else:
            print("%d는(은) 소수가 아닙니다"%number)
            break

number = int(input("정수 입력 : "))
judge(number)

    
