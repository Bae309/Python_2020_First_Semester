len1=int(input("첫번째 변의 길이 입력 : "))
len2=int(input("두번째 변의 길이 입력 : "))
len3=int(input("세번째 변의 길이 입력 : "))

if len1==len2==len3:
    print("정삼각형입니다")

elif len1>=len2+len3 or len2>=len1+len3 or len3>=len2+len1:
    print("삼각형이 성립될 수 없습니다")

elif len1==len2 or len2==len3 or len3==len1:

    if len1>=len2+len3 or len2>=len1+len3 or len3>=len2+len1:
        print("삼각형이 성립될 수 없습니다")

    else:
        print("이등변삼각형입니다")

elif len1**2==len2**2+len3**2 or len2**2==len1**2+len3**2 or len3**2==len1**2+len2**2:
    print("직각삼각형입니다")

else:
    print("일반삼각형입니다")


    
    
