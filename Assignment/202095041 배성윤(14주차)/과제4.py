def degree_change(num):

    Fahrenheit=((9/5)*num+32)

    return Fahrenheit

Celcius=int(input("섭씨 온도 입력 : "))

result=degree_change(Celcius)

print("화씨 온도는",result)
