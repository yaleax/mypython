class students:
    def __init__(self, id:int, name:str,score:float,age:int) -> None:
        self.id = id
        self.name = name
        self.score = score
        self.age = age
    def study(self) -> None:
        print(f"姓名{self.name}\n学号{self.id}\n年龄{self.age}\n成绩{self.score}")

if __name__ == "__main__":

    student1 = students(1001,'allen',90,18)
    student2 = students(1002,'宝儿姐',100,20)

    student1.study()
    print('====================')
    student2.study()