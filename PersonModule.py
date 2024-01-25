class Person:
    # def __init__(self): # 기본 생성자는 필수 X 
    #     print('Person 생성자 호출')
    #     pass
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person - name : {self.name}, age : {self.age}"

    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __gt__(self, other):
        return self.age > other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __eq__(self, other):
        return self.age == other.age
    
    def show(self):
        print(f"name : {self.name}, age : {self.age}")

    # 프로그램이 종료될 때 자동으로 호출
    def __del__(self):
        print("삭제 되었습니다")
