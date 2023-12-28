class Person:
    def __init__(self, name:str,sex:str = '男', habby:str = "抽烟,喝酒,烫头发") -> None:
        self.name = 'Joey'
        self.sex = sex
        self.habby = habby
    def eat(self) -> None:
        print(f"{self.name}在吃")

    def learn(self, infor: str) -> None:
        print(f"{self.name}在学习{infor}")

    def show_me(self) -> str:
        return f"我叫:{self.name},我的爱好是{self.habby}"


p1 = Person('Echo')
p1.eat()
p1.learn('Python')
p1.learn('Java')
print(p1.show_me())

 