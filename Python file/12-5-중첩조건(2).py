original_id='abc'
original-pwd='123'

input_id=input('ID입력:')
input_pwd=int(input("password 입력: "))

if original_id != input_id:
    print("로그인 실패 : ID오류")

else:
    if original_pwd != input_pwd:
        print("로그인 실패 : password오류")

    else:
        print("로그인 성공")
