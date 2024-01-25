# 사용자 정의 함수
def 함수명():
    print("함수호출")
    return True

a = 함수명()
print(a)

# 위치 인자를 이용한 함수의 호출
def restaurant(food, drink, dessert):
    return {'food' : food , 'drink' : drink, 'dessert' : dessert}

first = restaurant('스테이크', '와인', '치즈 케익')
print(first)

# 호출 시 매개변수의 이름을 함께 지정해서 순서에 상관없이 호출 가능 
second = restaurant(drink='소주', dessert='아이스크림',food='라면')
print(second)
print(1,2,3,4 , sep=',,')

# 기본 파라미터 : 매개변수의 초기값을 지정하는 것
def rest(food='스시', drink='콜라', dessert='빵'):
    return {'food' : food , 'drink' : drink, 'dessert' : dessert}

print(rest())
print(rest(food='국밥'))
print(rest(drink='사이다', dessert='프라페'))

c = 10
print(c)
def add(a, b):
    global c # 전역변수의 c를 쓰겠다
    c = a + b
    return c
print(add(1,2))
print(c)

# 파라미터를 튜플의 형태로 전달
def save_names(*args):
    print(args)

save_names('홍길동')
save_names('홍길동', '김개똥')

# 파라미터를 딕셔너리 형태로 전달
def save_names2(**kwargs):
    print(kwargs)

save_names2(이름 = '홍길동')
save_names2(이름 = '홍길동', 이름2 = '이말똥')

def myfunc1(a,b,*args):
    print(a, b, args)
myfunc1(1,2)
myfunc1(1,2,'a', 'b')

def myfunc2(a,b, **kwargs):
    print(a, b, kwargs)
myfunc2(1,2)
myfunc2(1,2,name="홍길동" , age=30)

def myfunc3(a, b, *args, **kwargs):
    print(a,b, args, kwargs)
myfunc3('a', 10, 'Hello', 20, name='홍길동')

def hi():
    print("Hello")

hello = hi
print(type(hello))
hello()

def mul(a, b):
    return a * b

def calc(func, a, b):
    print("결과 {}".format(func(a,b)))
calc(mul, 10, 5)
calc(add, 20, 5)