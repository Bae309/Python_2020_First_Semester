input_id=input("ID입력 : ")
input_password=input("Password 입력 :")

if len(input_id)<10:
    if len(input_password)<10:
        print("회원가입 성공")

    else:
        print("회원가입 실패 : password길이가 10을 초과")

else:
    print("회원가입 실패 : ID길이가 10 초과")
