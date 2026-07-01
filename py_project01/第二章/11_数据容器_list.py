#列表
# s = [56, 90 ,34,57,"A", "Hello", True]
# print(type(s))
# print(s[0])
# print(s[1])
# print(s[-1])
#
# s[4] = "B"
# print(s)
#
# del s[5]
# print(s)
#
# for i in s:
#     print(i)
# s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5])
# print(s[0:5:2])
# print(s[0:-2:1])
#
# s2 = ["23", "34", "545", "98", "45"]
# s3 = [23, 34, 545, 98, 45]
# s2.append(67)
# print(s2)
# s2.insert(1, "55")
# print(s2)
# s2.remove("23")
# print(s2)
# s2.pop(4)
# print(s2)
# s3.sort()
# print(s3)
# s3.reverse()
# print(s3)

# --------------------------------------- 列表 list 案例 --------------------------------------
#案例1. 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序, 输出其中的最小值、最大值 和 平均值。
# num_list = []
# for i in range(10):
#     num = int(input("请输入一个有效数字："))
#     num_list.append(num)
# print(num_list)
# num_list.sort()
# print("排序后的列表：", num_list)
# print("最小值：",num_list[0])
# print("最大值：",num_list[9])
# total = sum(num_list)
# avg = total / len(num_list)
# print("平均值为：", avg)

#案例2: 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# #合并列表
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的列表：", num_list1)
# new_list = [] #去重后的新列表
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print("去重后的列表：", new_list)

#案例2(简化): 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

#合并列表
# 解包: 将列表这一类容器解开成一个一个独立的元素
# 组包: 将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
# # num_list = num_list1 + num_list2
# print("合并后的列表：", num_list)
# new_list = [] #去重后的新列表
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print("去重后的列表：", new_list)

# 案例3: 生成1-20的平方列表。 --> range(1,21)
num_list = []
for num in range(1,21):
    num_list.append(num**2)
print("生成的列表：",num_list)
#方式二: 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1: [要插入的值 for i in 序列/列表]
num_list2 = [i**2 for i in range(1,21)]
print("生成的列表：",num_list2)

#案例4: 从一个数字列表中提取所有偶数，并计算其平方，组成一个新列表。 ---> 判断偶数: num % 2 == 0
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
num_list3 = [i**2 for i in num_list if i%2==0]
print(num_list3)




