print("10 + 4 = ", 10 + 4)  # 加
print("10 - 4 = ", 10 - 4)  # 减
print("10 * 4 = ", 10 * 4)  # 乘
print("10 / 4 = ", 10 / 4)  # 除 - 2.5
print("10 // 4 = ", 10 // 4) # 整除(结果为整数) - 2
print("10 % 4 = ", 10 % 4)  # 取余/求模 - 2
print("10 ** 4 = ", 10 ** 4) # 幂指数, 10的4次方 - 10000

#x = input("请输入x的值：")
#y = input("请输入Y的值：")

# 案例: 输入两个数 x 和 y , 计算 x + y 以及 x - y 的结果并输出
#print(f"x + y = {int(x)+int(y)}")
#print(f"x - y = {int(x)-int(y)}")

#计算输入的三个整数的平均数
# a = int(input("请输入a的值："))
# b = int(input("请输入b的值："))
# c = int(input("请输入c的值："))
# average = (a+b+c)/3
# print(f"这三个数的平均值为：{average}")

num = 85

num +=10
print(f"num += 10后的值为{num}")

num -=10
print(f"num -= 10后的值为{num}")

num *=10
print(f"num *= 10后的值为{num}")

num /=10
print(f"num /= 10后的值为{num}")

num //=10
print(f"num //= 10后的值为{num}")

num %=3
print(f"num %= 10后的值为{num}")

num **=3
print(f"num **= 10后的值为{num}")

print("100 == 100吗？", 100 == 100)
print("100 != 100吗？", 100 != 100)
print("100 < 100吗？", 100 < 100)
print("100 > 100吗？", 100 > 100)
print("100 >= 100吗？", 100 >= 100)
print("100 <= 100吗？", 100 <= 100)

a = int(input("请输入一个数字："))
print(f"{a}在10-20之间：", 10 <= a <= 20)
print(f"{a}在10-20之间：", a <= 10 or a >= 20)

