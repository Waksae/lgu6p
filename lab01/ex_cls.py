class Person:
    def __init__(self, name, height, weight):        # __init__와 self는 지켜서 작성할 것. 문법.
        self.name = name
        self.height = height
        self.weight = weight

    def speed(self):
        self.print()
        return (self.height / self.weight) * 5
    
    def print(self):
        print(f"나는 {self.name}이고 키{self.height}, 몸무게{self.weight}입니다.")
    
p1 = Person("Tom", 170, 100)
p2 = Person("Kim", 180, 110)

print(type(p1))

print(p1.name)
print(p2.name)
print(p1)
print(p2)
