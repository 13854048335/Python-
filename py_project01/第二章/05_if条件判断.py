#if条件判断：如果分数超过680分，我就去清华读书
# score = 700
# if score >= 680:
#     print("欢迎来到清华读书")
# print("---------------------------")
#
# ok_user = "1888888888"
# ok_password = "666888"
# user = input("请输入用户名：")
# pwd = input("请输入密码：")
# if user == ok_user and pwd == ok_password:
#     print("登录成功!")
# else:
#     print("用户名或密码错误请重新输入!")

#案例：根据用户输入的年份，判断这个年份是闰年还是平年
#（非整百年份且能被四整除的是闰年，整百年份必须被400整除才是闰年）
# year = int(input("请输入年份："));
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}年是闰年")
# else:
#     print(f"{year}年是平年")

# num = int(input("请输入数字："));
# if num > 0:
#     print(f"{num}是正数")
# elif num < 0:
#     print(f"{num}是负数")
# else:
#     print(f"num是{num}")
# user = input("请输入用户名：")
# pwd = input("请输入密码：")
# if user == "admin" and pwd == "666888":
#     print("登录成功")
# elif user == "root" and pwd == "547527":
#     print("登录成功")
# elif user == "zhangsan" and pwd == "123456":
#     print("登录成功")
# else:
#     print("登录失败，用户名或密码错误")
"""
案例: 三角形类型判断：根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角形 ，还是不能构成三角形。
    1. 构成三角形的条件：两边之和大于第三边
    2. 三角形判定规则：
        三个边都相等: 等边三角形
        两个边相等: 等腰三角形
        三个边都不相等: 普通三角形
"""
# 1. 接收输入的三角形三个边的边长
a = int(input("请输入三角形的第一条边："));
b = int(input("请输入三角形的第二条边："));
c = int(input("请输入三角形的第三条边："));

if a + b > c or a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a},{b},{c}这三条边构成等边三角形")
    elif a == b or b == c or c == a:
        print(f"{a},{b},{c}这三条边构成等腰三角形")
    else:
        print(f"{a},{b},{c}这三条边构成普通三角形")
else:
    print(f"{a},{b},{c}这三条边无法构成三角形请重新输入!")









