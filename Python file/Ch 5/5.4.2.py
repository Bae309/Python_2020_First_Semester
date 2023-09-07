num=int(input("숫자 입력 : "))

pnum=[]

for i in range(1, num+1):
     dcount=0

     for j in range(1,i+1):

          if i%j==0:
               dcount=dcount+1

     if dcount==2:
          pnum.append(i)

print("1~",num,"까지의 소수의 리스트 : ",pnum)
print("1~",num,"까지의 소수의 개수 : ",len(pnum))
