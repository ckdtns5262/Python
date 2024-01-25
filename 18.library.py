# import 
# 모듈은 파이썬 코드를 작성 해놓은 스크립트 파일
# 스크립트 파일에는 클래스, 함수, 변수 등이 정의되어 있다.
# 외부 모듈을 가져와서 사용할 때는 import 명령을 사용한다.

import math
print(math.sqrt(2)) # 제곱근을 구하는 함수
print(math.pow(2,3)) # 2의 3승을 구하는 함수
# 주요함수
# ceil(x) : 올림 
# floor(x) : 내림 
# fabs(x) : x의 절대값
# trunc(x) : x의 소수점 이하 버림

import os
# print(os.getcwd())
# os.system("clear") 터미널 창 clear 시켜줌 
# print(os.listdir("/Users"))

import time
before = time.time()
print(before)
# time.sleep(1) 1초 동안 프로그램 멈추고 실행
after = time.time()
print(after - before)

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.date())
print(now.minute)
print(now.second)

import calendar
print(calendar.calendar(2024)) # 2024년 전체 달력
print(calendar.month(2024, 1)) # 2024년 1월 달력만 

import random
print(random.random()) # 0에서 1미만의 실수 하나 생성
print(random.randint(1,10)) # 1에서 10사이의 정수 난수 하나 생성(end 포함)

a = ['가위', '바위', '보']
print(random.choice(a)) # 리스트에서 임의의 요소를 하나 골라 리턴
random.shuffle(a) # 리스트의 요소를 무작위로 섞는다
print(a)

