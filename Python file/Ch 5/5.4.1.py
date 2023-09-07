list1=[[11,33,22,7],[77,2,90],[3,66,44,9,8]]

minvalue=min(list[0])

for i in range(len(list1)):

    print((i+1),"번째 줄의 합계 : ",sum(list1[i])

    if minvalue > min(list1[i]):
          minvalue=min(list1[i])

print("리스트에서 가장 작은 값은 : ",minvalue)
