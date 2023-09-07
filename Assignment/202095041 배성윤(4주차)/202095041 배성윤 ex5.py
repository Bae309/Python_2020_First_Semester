num=int(input("사용자 입력 : "))
i=0
cnt=0
sum=0
while True :
     i=i+1
     if (i%3 != 0) :
          continue
     else :
          cnt=cnt+1
     if (i>num):
          break
     sum=sum+i

print(num,"을 넘었을 때의 값 : ",i)
print(num,"을 넘었을 때까지의 총합계 : ",sum)
print(num,"을 넘었을 때까지 몇번째 3의 배수인가 : ",cnt)
