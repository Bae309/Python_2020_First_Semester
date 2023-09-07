price_pencil=1000
price_pen=2000

num_pencil=int(input("연필의 갯수: "))
num_pen=int(input("펜의 갯수: "))

total_price=price_pencil*num_pencil+price_pen*num_pen
if total_price>10000:
    total_price=total_price*0.9
    print("10% 할인")

print("총합 :",int(total_price),"원")
