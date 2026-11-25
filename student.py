#定义 Student 学生类
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def to_dict(self):
        return {"name":self.name,"age":self.age,"score":self.score}

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["age"],data["score"])

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}，成绩：{self.score}"