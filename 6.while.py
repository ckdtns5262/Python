# 반복문 while

num = 1
while num < 10:
    print(num)
    num = num + 1

# 1 ~ 100 사이의 정수 중 홀수의 합과 짝수의 합을 각각 구하세요 
hol = 0
jak = 0
while num < 101:
    if num % 2 == 0:
        hol += num
    else:
        jak += num
    num += 1
print(f'홀수의 합은 {hol}')
print(f'짝수의 합은 {jak}')