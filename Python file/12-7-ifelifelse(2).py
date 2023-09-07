eng=int(input("영어점수 : "))
math=int(input("수학점수 : "))

total=eng+math

if total<110:
    print("불합격 : 총점 부족")

elif eng>=40:
    if math>=40:
        print("합격")
    else:
        print("불합격 : 수학 점수 부족")

else:
    print("불합격 : 영어 점수 부족")
