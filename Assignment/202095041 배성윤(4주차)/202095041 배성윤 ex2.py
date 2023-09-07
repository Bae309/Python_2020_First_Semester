first=int(input("첫번째 숫자 입력 : "))
second=int(input("두번째 숫자 입력 : "))

while first > second :

    temp=first
    first=second
    second=temp

print(first,"부터",second,"까지의 홀수값의 합은 :",end=' ')

sum=0
while first <= second :
    if first % 2 == 1:
        sum=sum+first
        first=first+2


print(sum)
