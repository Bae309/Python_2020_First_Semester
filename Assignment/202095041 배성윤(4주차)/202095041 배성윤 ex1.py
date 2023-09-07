hap=0
avg=0.0
i=0

while True:
    kor=int(input("국어점수 입력 : "))
    eng=int(input("영어점수 입력 : "))
    math=int(input("수학점수 입력 : "))

    hap=kor+eng+math
    avg=hap/3

    if(kor==0 and eng==0 and math==0):
                break

    else:
                print(str(i+1)+"번째 학생 : 총점 {}점, 평균 {}점".format(hap,avg))
                i+=1

print("총 {}명을 성적처리 하였습니다. ".format(i))
    
