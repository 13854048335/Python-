# 练习任务：
#
# Hello World
#
# 需求：让程序打印出问候语
# 思路：使用print函数，尝试打印多行文字
# 个人信息展示
# 个人信息展示
print("=" * 30)
print("        欢迎光临")
print("=" * 30)
print("姓名：张三")
print("年龄：25岁")
print("职业：Python开发工程师")
print("邮箱：zhangsan@example.com")
print("电话：138-0000-0000")
print("=" * 30)
print("        感谢访问")
print("=" * 30)

#
# 需求：用变量存储姓名和年龄，然后输出
# 思路：创建变量 → 赋值 → 打印，尝试用不同方式拼接字符串
# 变量交换
name = "张三"
age = 25
job = "Python开发工程师"
email = "zhangsan@example.com"
phone = "138-0000-0000"
print("=" * 40)
print(f"{'个人信息展示':^38}")
print("=" * 40)
print(f"姓名：{name}")
print(f"年龄：{age}岁")
print(f"职业：{job}")
print(f"邮箱：{email}")
print(f"电话：{phone}")
print("=" * 40)
print(f"{'祝您愉快！':^38}")
print("=" * 40)

# 需求：交换两个变量的值并输出交换前后的结果
# 思路：1) 创建两个变量赋值 2) 使用临时变量或Python特有方式交换 3) 打印验证
# 创建两个变量并赋值
a = 10
b = 20

print(f"交换前：a = {a}, b = {b}")

# 使用临时变量进行交换
temp = a
a = b
b = temp

print(f"交换后：a = {a}, b = {b}")

# 简单计算器
#
# 需求：输入两个数字，输出四则运算结果
# 思路：1) 使用input获取两个数字 2) 进行类型转换 3) 计算并输出结果
# 简单计算器 - 基础版
print("=" * 40)
print("        简单计算器")
print("=" * 40)

# 获取用户输入
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

# 四则运算
print("\n计算结果：")
print("=" * 40)
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")

# 除法需要判断除数是否为0
if num2 != 0:
    print(f"{num1} ÷ {num2} = {num1 / num2}")
else:
    print(f"{num1} ÷ {num2} = 除数不能为0！")
print("=" * 40)