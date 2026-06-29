#案例：银行卡ATM取款

total = 10000

#1.输入密码
password = input("请输入密码:")
#2.计算余额
money = input("请输入取款金额:")
#3.计算余额并输出
Balance = int(total) -int(money)
print(f"余额为：{Balance}")