def gugu(dan):

    hap=0
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)

    for j in range(1,10):
        hap=hap+dan*j
    return hap

dan=int(input("구구단 출력을 원하는 단 입력:"))
total=gugu(dan)
print(dan,"단의 모든 결과의 합계는 : ",total)
