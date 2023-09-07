first=1
sum=0

for num in range (1,11) :
     second=10*num

     while first <= second :
          sum=sum+first
          first=first+1

     print("1-",second,":",sum)
