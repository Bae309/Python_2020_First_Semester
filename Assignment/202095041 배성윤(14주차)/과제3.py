def train_ticket(city):

    if(city=='부산'):
        print(city,"까지의 금액은 30000원 입니다.")

    if(city=='대구'):
        print(city,"까지의 금액은 2000원 입니다.")

    if(city=='수원'):
        print(city,"까지의 금액은 10000원 입니다.")

    if(city=='춘천'):
        print(city,"까지의 금액은 5000원 입니다.")

region=input("춘천(5000원)/부산(30000원)/대구(2000원)/수원(10000원) : ")

train_ticket(region)

