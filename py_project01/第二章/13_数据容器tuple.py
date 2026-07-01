# 元组基本操作 - tuple ---> 元素可以重复, 有序, 不可修改
# t = (1, 3, 45, 32)
# print(t)
# print(type(t))
#
# #索引
# print(t[1])
# #切片
# print(t[0:2:1])
# print(t.count(45))
# print(t.index(45))
# --------------------------------------------- 元组 tuple 组包与解包 ---------------------------------------------------
# 组包操作
# t1 = (5, 7, 9, 10, 2, 23, 12)
# t2 = 5, 7, 9, 10, 2, 23, 12
# print(t1)
# print(t2)
#
# #解包操作
# #基础解包(变量数量与容器的元素个数一致)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
# #* 扩展解包 (* 收集剩余的所有元素, 封装列表list中)
# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)

"""
    根据如下提供的学生成绩单，完成如下需求：
        1. 计算每个学生的总分、各科平均分，然后一并输出出来。
        2. 统计各科成绩的最低分、最高分、平均分，并输出。
        3. 查找成绩优秀（平均分大于90）的学生，并输出。
"""
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
#1. 计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")

#2. 统计各科成绩的最低分、最高分、平均分，并输出。
chiese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文最高分{max(chiese_scores)}, 语文最低分{min(chiese_scores)}")
print(f"数学最低分: {min(math_scores)}, 最高分:  {max(math_scores)}, 平均分: {sum(math_scores)/len(math_scores)}")
print(f"英语最低分: {min(english_scores)}, 最高分:  {max(english_scores)}, 平均分: {sum(english_scores)/len(english_scores)}")
#3. 查找成绩优秀（平均分大于90）的学生，并输出
print("优秀学生(平均分 > 90)名单如下: ")
# 方式一:
# for s in students:
#      total = s[2] + s[3] + s[4]
#      avg = total / 3
#      if avg > 90: # 优秀学生
#          print(f"学号: {s[0]}, 姓名: {s[1]}, 平均分: {avg:.1f}")
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90: # 优秀学生
        print(f"学号: {id}, 姓名: {name}, 平均分: {avg:.1f}")
