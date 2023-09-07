""" 프로그램 제목 : 점수 총점과 평균 구하기
    작성자 : 배성윤
    작성일 : 2020.3.31"""

a=int(input("과목1 점수 입력 : "))
b=int(input("과목2 점수 입력 : "))
c=int(input("과목3 점수 입력 : "))
d=int(input("과목4 점수 입력 : "))
e=int(input("과목5 점수 입력 : "))

total=a+b+c+d+e
average=(a+b+c+d+e)/5

print("점수 총점은 : " , total);print("점수 평균은 : " , average)
