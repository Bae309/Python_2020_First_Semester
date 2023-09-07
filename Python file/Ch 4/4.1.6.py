kor=int(input("국어 점수를 입력 : "))
eng=int(input("영어 점수를 입력 : "))
math=int(input("수학 점수를 입력 : "))

avg=(kor+eng+math)/3

if avg >= 95 :
     print("당신의 평균은 {}점 입니다. ".format(avg))
     print("축하합니다. A+입니다.")

print("감사합니다")
