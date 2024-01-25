a = {}
print(a, type(a))

a = dict()
print(a, type(a))

a = {"name" : "홍길동", "age" : 32}
print(a)

print(a["name"])
a["name"] = "홍길순"
print(a)

# 요소 삭제
del a["name"]
print(a)

# 요소 추가 
a["name"] = "홍길동"
print(a)
# 요소 삭제
print(a.pop("name"))
print(a)

# 딕셔너리 합치기 
a = {"name" : "홍길동"}
b = {"age" : 20}
c = {"country" : 'KOR'}

a.update(b)
print(a)
a.update(c)
print(a)

# 키만 가져오기
print(a.keys())

for key in a.keys():
    print(key)

# 값만 가져오기 
print(a.values())

for val in a.values():
    print(val)

# 키와 값을 모두 가져오기 
print(a.items())

print(a["name"])
# print(a["name2"])

print(a.get("name"))
print(a.get("name2"))

# 요소 포함 여부 
print("name" in a)
print("name2" in a)