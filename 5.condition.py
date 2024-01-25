a = 3
b = 5
c = 4
if a < b < c:
    print(f'{a}는 {b}보다 작고 {b}는 {c}보다 작습니다')
elif a < b and b > c:
    pass
    #print(f'{a}는 {b}보다 작고 {b}는 {c}보다 큽니다')
else:
    print('else문 실행')
print('프로그램 종료')

str1 = "abcdef"
if "h" in str1:
    print('있음')
else:
    print('없음')

list = ["홍길동", "이춘향", "박둘리"]
if "홍길동" in list:
    print("홍길동 있음")
elif "이춘향" in list:
    print("이춘향 있음")
elif "박둘리" in list:
    print("박둘리 있음")
else:
    print("없음")