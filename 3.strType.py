a = "Hello Python"
print(a, type(a))

a = '"Hello Python"'
print(a, type(a))

# 이스케이프 문자 
# \n 줄바꿈
# \t 탭 문자 
# \\ 역슬래시
# \' 따옴표
# \" 쌍따옴표
b = """Hello 
Python""" # 따옴표 3개로 묶으면 줄바꿈이 가능
print(b)

a = 'Hello'
b = 'World'
print(a + ' ' +  b)
a = "*" * 40
print(a)

# 문자열 인덱싱
a = "test python string"
print(a[0])
print(a[-1]) # 음수로 주면 마지막 인덱스부터 가져온다

# 문자열 슬라이싱 
print(a[0:2]) # 0번 인덱스부터 2번 인덱스 바로 앞(1번 인덱스)까지
print(a[0:11]) # 0번 인덱스부터 11번 인덱스 바로 앞(10번 인덱스)까지
print(a[0:1000]) # 범위를 넘어도 오류가 발생하지 않음
print(a[:11]) # 앞의 숫자를 생략하면 제일 처음부터
print(a[5:]) # 뒤의 숫자를 생략하면 제일 마지막까지
print(a[:]) # 처음부터 끝까지

# 문자열 포매팅
# %s : 문자열
# %c : 문자 1개
# %d : 정수 
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : %문자

old = 30
a = "나는 %d살 입니다"%old 
height = 176.9
a = "나는 %d살 이고 키는 %fcm 입니다"%(old,height)
print(a)

# 포메팅 : 문자열 내에 {}괄호를 입력하고 format 함수의 인수로 삽입할 변수,
# 값을 입력하면 {}괄호 자리에 차례대로 인수를 전달한다.
a = "나는 {}살 이고 키는 {}cm 입니다.".format(old, height)
print(a)
a = "숫자 {}, {}, {}".format(1,2,3)
print(a)
# {} 괄호 안에 0부터 시작하는 순서 값을 지정할 수 있다.
a = "숫자 {2}, {1}, {0}".format(1,2,3)
print(a)

name = "홍길동"
country = "한국"
age = 25
print(f"나는 {country}사람이고 이름은 {name}이며 나이는 {age}살인 사람입니다")

str1 = "%10s" % "hi" # 10자릿수를 맞춘다
print(str1)

number = "%5.2f" % 3.141592 # 소수점 x자리까지 출력하고 싶을때
print(number)
# %%
