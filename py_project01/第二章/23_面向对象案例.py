# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"
    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
# 教务管理系统类
class EduManagement:
    system_version = 1.0
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = []
    # 添加学生成绩
    def add_student(self):
        name =  input("请输入学生姓名：")
        # 判断学生的姓名是否存在，存在则添加失败
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在，添加失败")
                return
        chinese = int(input("请输入学生的语文成绩："))
        math = int(input("请输入学生的数学成绩："))
        english = int(input("请输入学生的英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english);
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生的各科成绩必须要在0-100之间")
            return

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("当前学生成绩：",s)
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print("修改后的学生成绩：", s)
                    return
                else:
                    print("学生的各科成绩必须要在0-100之间")
                    return
        print("未找到该学生修改失败")
    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生修改失败")
    # 查询指定的学生成绩
    def query_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("学生信息：",s)
        print("未找到该学生修改失败")
    # 展示学生成绩
    def list_student(self):
        for s in self.student_list:
            print("学生信息：", s)
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
        while True:
            print()
            print("1.添加学生成绩, 2.修改学生成绩, 3.删除学生成绩, 4.查询学生成绩, 5.查询所有学生成绩，6.退出")
            choice = input("请选择要进行的操作（1-6）：")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("拜拜")
                        break
                    case _:
                        print("选择的操作不合法")
            except ValueError as e:
                print("输入的数据有问题，请检查后重新输入")
            except Exception as e:
                print("程序运行出错了，请重新选择")





if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()




