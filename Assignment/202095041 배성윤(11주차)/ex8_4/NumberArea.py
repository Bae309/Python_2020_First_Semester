def aliquot(n):

    if a % x == 0:
        print(n,"의 약수 : ",x)
        

def prime(n):

    i=2

    while i<n:
        if n%i==0 :
            break

    if i==n:
        print(n,"의 소수? : True")

    else:
        print(n,"의 소수? : False")

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

    print(n,"의 팩토리얼 값 : ",fact(n))

def Pnum(n):
    total=0

    for i in range(1,int(n/2*1)):
        if n%i==0:
            total=total+i

        if total == n :
            print("True")

        else:
            print("False")
