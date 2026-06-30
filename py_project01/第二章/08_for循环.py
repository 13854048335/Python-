# for循环: 遍历输入的字符串
msg = "Hello World"
for char in msg:
    print(f"元素：{char}")
else:
    print("遍历结束")
total = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i
# for i in range(1, 101, 2):
#      total += i
# print("1-100之间的奇数累加之和: ", total)
for i in range(100, 501):
    if i % 3 == 0:
      total += i
print("100-500 之间所有3的倍数的数字之和:  ", total)

"""
    循环嵌套: 根据输入的长方形的长度 m, 宽度 n , 打印一个长方形 ;

    如下: 是一个长度为10 , 宽度为5 的长方形
     *  *  *  *  *  *  *  *  *  *
     *  *  *  *  *  *  *  *  *  *
     *  *  *  *  *  *  *  *  *  *
     *  *  *  *  *  *  *  *  *  *
     *  *  *  *  *  *  *  *  *  *

     print("*") : 自带换行效果 , 每一次执行都会输出新的一行中 ;
     print("*", end=""): end表示的是每一次输出以什么结束; 默认 \n, 表示换行 .
"""
#长度
# m = int(input("请输入长方形的长："))
# #宽度
# n = int(input("请输入长方形的宽："))
# for num in range(n):
#   for i in range(m):
#     print("*", end="  ")
#   print()
# 嵌套循环案例: 打印99乘法表
for i in range(1,10):# 外层循环 - 控制行
    for j in range(1,i+1): #内层循环 - 控制列
        print(f"{j} x {i} = {j * i}", end="\t")
    print()


