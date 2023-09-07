num=int(input("배수 숫자 입력 : "))

i=0
hap=0

while i <100 :
     i=i+1
     if (i%num) != 0:
          continue
     hap=hap+i

print("1부터 100까지 {}의 배수의 합은 : {}".format(num,hap))
