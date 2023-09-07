num=int(input("팩토리얼 숫자 입력 : "))

fac=1

for i in range(num,0,-1) :
     fac=fac*i

print("%d의 팩토리얼 값은 : "%num, fac)
