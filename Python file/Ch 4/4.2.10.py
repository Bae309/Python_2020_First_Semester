hap=0
count=0

while True  :
     num=int(input("숫자를 입력 : "))
     hap=hap+num
     count=count+1
     if hap >= 1000 :
             break

print("1000을 넘은 수 : ",hap,end=' ')
print(", 평균은 : ",hap/count)
             
