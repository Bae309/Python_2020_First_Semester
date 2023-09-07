num=int(input("숫자 입력 : "))

list=[]

for i in range(1,num+1):
    if num% i ==0:
        list.append(i)

print(num,"의 약수는",list,"입니다.")
