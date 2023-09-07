num=int(input("숫자 입력: "))

for i in range(1,num+1):
    j=1
    while j <= i:
        print("*",end='')
        j=j+1

    print()
    i += 1
