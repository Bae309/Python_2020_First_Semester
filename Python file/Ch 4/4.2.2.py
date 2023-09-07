first=int(input("첫번째 숫자 입력 : "))
second=int(input("두번째 숫자 입력 : "))

if first > second :

     temp=first
     first=second
     second=temp

print(first,"부터",second,"까지의 합은 : ",end=' ')

sum=0
while first <= second :
     sum=sum+first
     first=first+1


print(sum)
