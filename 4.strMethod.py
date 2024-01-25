# 문자열 슬라이싱
# [:] : 처음부터 끝까지
# [start:] : start부터 끝까지 
# [:end] : 처음부터 end-1까지 
# [start:end] : start부터 end-1까지 
# [start:end:step] : step만큼 건너뛰면서 start부터 end-1까지

test = "abcd 가나다라마바사 あいうえお"
print(test[0])
print(test[5:12])
# find(), index()는 인덱스 값을 리턴 
print(test.find("가나다라"))
print(test.find("카")) # 값이 없으면 -1을 리턴
print(test.index("나"))
# print(test.index("카")) # 값이 없으면 오류 발생 

path = "users\\ichanghyun\\desktop\\abc.jpg"
print(path)
print(path.rfind("\\"))
# 경로를 제외하고 파일명을 출력 
print(path[path.rfind("\\")+1:])

# split (리스트 형식으로 리턴)
print(path.split("\\"))

# replace (치환)
greet = "안녕하세요 파이썬 입니다"
print(greet.replace("안녕하세요" , "Hello Python"))

# strip (공백을 제거해줌)
a = "     test      "
print(a.strip())

a = "abcd"
print(a.upper()) # 대문자로 변환 
b = "ABCd"
print(b.lower()) # 소문자로 변환
c = "aaaaaaaaaaaabbbbbbbbbbcccccccccccccccddddddddddde1"
print(c.count('aa')) # aa가 포함된 문자열의 갯수를 반환 
print(len(c)) # 문자열의 길이를 반환
print(c.isalpha()) # 알파벳이면 True
a = "abcd"
print(a.islower()) # 소문자이면 True
print(a.isupper()) # 대문자이면 True
a = "1234"
print(a.isdecimal()) # 10진수인지 판단
print(a.isdigit()) # 아라비아 숫자인지 판단
print(a.isnumeric()) # 수 자체인지 판단

print(dir(str)) # str의 모든 함수를 출력
print(dir(int)) # int의 모든 함수를 출력