import random
"""
成绩判断

需求：输入分数，输出对应等级
思路：
1) 获取分数输入
2) 使用if-elif-else判断等级
3) 输出等级结果
"""
score = int(input("请输入分数："))
if 90 <= score <= 100:
    print("优秀")
elif  70 <= score < 90:
    print("良好")
elif 60 <= score < 70:
    print("及格")
else:
    print("不及格")

"""
乘法表

需求：打印九九乘法表
思路：
1)外层循环控制行 
2)内层循环控制列 
3)格式化输出
"""
print("--------------")
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} x {i} ={j * i}", end="\t")
    print()
print("--------------")
"""
猜数字游戏

需求：实现猜数字游戏
思路：1) 生成随机数 2) 循环获取用户猜测 3) 给出提示直到猜中
"""
random_num = random.randint(1, 100)
while True:
    num = int(input("请输入你猜的数字："))
    if num > random_num:
        print("你猜大了")
    elif num < random_num:
        print("你猜小了")
    else:
        print("恭喜你猜对了")
        break



