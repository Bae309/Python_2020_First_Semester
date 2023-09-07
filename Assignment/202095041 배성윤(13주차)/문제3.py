num=int(input("양의 정수 입력 : "))
hap=0

for i in range(1,num+1):
    if i %2==0:
        hap=hap+i

print("1부터 ",num,"까지 짝수들의 합은",hap,"입니다.")
