st=input("영어 문장을 입력 :")

print("입력된 문장의 길이는 : ",len(st))
print("각 단어의 첫 문자를 대문자로 변환 : ",st.title())
print("모든 글자를 대문자로 변환 : ",st.upper())
print("문자열에 a가 몇번 나타나는가? : ",st.count('a'))
print("입력된 문자열이 모두 문자로만 구성되었는가? : ",st.isalpha())
print("입력된 문자열이 모두 숫자로만 구성되었는가? : ", st.isdigit())
print("입력된 문자열이 모두 대문자 구성되었는가? : ", st.isupper())
