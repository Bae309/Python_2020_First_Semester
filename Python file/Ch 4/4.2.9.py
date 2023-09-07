subject=1
total=0

while subject <= 5 :

     score=int(input(str(subject)+"번째 성적 입력 : "))

     if (score >=0 and score <= 100) :
          total=total+score
          print(subject,"번째 성적 :",score)
          subject=subject+1

     else:
          print("유효한 성적이 아닙니다")

else :
     print("총점 :", total)
     print("평균 :", total/5)
