sem=int(input("수료 학기 입력 : "))
avg=float(input("평균 학점 입력 : "))

if sem<1 or sem>8:
    print("장학금 지급 대상이 아닙니다.")

else:
    if avg >= 4:
        print("전액장학금 지급")

    if avg >= 3.5:
        print("50% 장학금 지급")

    if avg >= 3.0:
        print("30% 장학금 지급")

    else :
        print("장학금을 지급할 수 없습니다.")
