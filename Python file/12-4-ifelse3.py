price_tshirt=10000
price_sweater=30000

num_tshirt=int(input("티셔츠 개수:"))
num_sweater=int(input("스웨터 개수:"))

total=price_tshirt*num_tshirt+price_sweater*num_sweater

if total<=100000:
    total=total*0.95

else:
    total=total*0.85

print("총 가격은",total,"원")
