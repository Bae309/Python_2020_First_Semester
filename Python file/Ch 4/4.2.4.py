multi=int(input("합을 원하는 배수 입력 : "))
hap=0

for i in range(multi,1001,multi) :

     hap=hap+i

print("1부터 100까지의 {}의 배수의 합은 : {}".format(multi,hap))
