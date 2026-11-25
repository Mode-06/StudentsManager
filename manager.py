#学生管理、增删改查、统计和文件保存
import json
from pathlib import Path
from student import Student

class StudentManager:
    def __init__(self,filename=r"C:\Users\窦梓洋\Desktop\Python学习\d21.student.json"):
        self.filename=filename
        self.students=[]
        self.load_stu()

    #内部查找
    def __find_stu(self,name):
        for i in self.students:
            if i.name==name:
                return i
        return None

    #读文件
    def load_stu(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as f:
                data=json.load(f)
        except FileNotFoundError:
            self.students=[]
            return
        except json.JSONDecodeError:
            self.students=[]
            return
        self.students=[Student.from_dict(item) for item in data]

    #存
    def save_stu(self):
        path=Path(self.filename)
        tmp=Path(str(path)+".tmp")
        with open(tmp,"w",encoding="utf-8") as f:
            json.dump([i.to_dict() for i in self.students],f,ensure_ascii=False,indent=4)
        tmp.replace(path)

    #增
    def add_stu(self):
        name=input("请输入姓名：").strip()
        if not name:
            print("姓名不能为空！")
            return
        elif self.__find_stu(name):
            print("该姓名已存在！")
            return
        try:
            age=int(input("请输入年龄："))
            score=int(input("请输入成绩："))
        except ValueError:
            print("请输入数字！")
            return
        self.students.append(Student(name,age,score))
        self.save_stu()
        print("\n添加成功！")

    #查看所有学生
    def show_stu(self):
        if not self.students:
            print("暂无数据")
            return
        print(f"共{len(self.students)}名学生")
        for i,j in enumerate(self.students,1):
            print(f"{i}.{j}")

    #查
    def search_stu(self):
        name=input("请输入姓名：").strip()
        stu=self.__find_stu(name)
        if stu is None:
            print("\n该学生不存在！")
        else:
            print()
            print(stu)

    #改
    def update_stu(self):
        name=input("请输入姓名：").strip()
        stu=self.__find_stu(name)
        if stu is None:
            print("学生不存在！")
            return
        age=int(input("请输入年龄："))
        score=int(input("请输入成绩："))
        stu.age=age
        stu.score=score
        self.save_stu()
        print("\n修改成功！")

    #删
    def delete_stu(self):
        name=input("请输入姓名：").strip()
        stu=self.__find_stu(name)
        if stu is None:
            print("学生不存在！")
            return
        ans=input(f"确认删除学生{name}吗？(y/n)：")
        if ans=='n' or ans=='N':
            print("已取消删除！")
        elif ans=='y' or ans=='Y':
            self.students.remove(stu)
            self.save_stu()
            print("删除成功！")

    #统计
    def count_stu(self):
        if not self.students:
            print("暂无数据！")
            return
        cscores=[s.score for s in self.students]
        highest=max(self.students,key=lambda s:s.score)
        lowest=min(self.students,key=lambda s:s.score)
        print(f"学生人数：{len(self.students)}")
        print(f"平均成绩：{sum(cscores)/len(self.students):.1f}")
        print(f"最高分：{highest.name}（{highest.score}分）")
        print(f"最低分：{lowest.name}（{lowest.score}分）")
        print(f"及格人数：{sum(1 for x in cscores if x >= 60)}")
        print(f"优秀人数：{sum(1 for x in cscores if x >= 90)}")
        print()
        rank=sorted(self.students,key=lambda s:s.score,reverse=False)
        print("----------成绩排行榜----------")
        for i,s in enumerate(rank,1):
            print(f"第{i}名:{s.name}，{s.score}分")