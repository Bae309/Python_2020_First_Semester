first=1
sum=0
num=1

while (num <=10) :
     second=10*num
     num=num+1

     while first <= second :
          sum=sum+first
          first=first+1

     print("1-",second,":",sum)
