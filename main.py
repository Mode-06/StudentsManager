from manager import StudentManager

def menu():
    print("""========== 学生信息管理系统 ==========

    1. 添加学生
    2. 查看所有学生
    3. 查询学生
    4. 修改学生
    5. 删除学生
    6. 成绩统计
    0. 退出程序

    """)

def main():
    print("第二次提交测试！")
    sm=StudentManager()
    while True:
        menu()
        choice = input("请输入操作：").strip()
        print()
        
        if choice == "0":
            sm.save_stu()
            print("数据已保存，程序结束\n")
            break
        elif choice == "1":
            sm.add_stu()
        elif choice == "2":
            sm.show_stu()
        elif choice == "3":
            sm.search_stu()
        elif choice == "4":
            sm.update_stu()
        elif choice == "5":
            sm.delete_stu()
        elif choice == "6":
            sm.count_stu()
        else:
            print("请输入 0-6！")

        print()


if __name__ == "__main__":
    main()