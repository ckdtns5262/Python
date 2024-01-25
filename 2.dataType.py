# 파이썬의 데이터 타입 
# 1. 논리형 : True, False
# 2. 정수형 : 10진수, 2진수(0b, 0B), 8진수(0o, 0O), 16진수(ox, 0X)
# 3. 실수 : 소수점이 있는 수 
# 4. 복소수 : 제곱해서 음수가 되는 수 
# 5. 문자열 

# 논리형 (bool)
a = True
print(a)
b = False
print(b)
print(type(a), type(b))
a = bool(True)
a = bool(2)
print(a)

# 정수형 (int)
a = 10
print(type(a))
a = int(20)
print(a, type(a))

# 실수 (float)
a = 10.1
print(a, type(a))

# 산술 연산자
a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 몫을 구함
print(a % b)
print(a ** b)