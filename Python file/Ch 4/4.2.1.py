n=int(input("합계를 원하는 숫자 입력 : "))

i=1
hap=0

while i <= n :
     hap=hap+i
     i=i+1

print("1부터 {}까지의 합은  : {}".format(n,hap))
