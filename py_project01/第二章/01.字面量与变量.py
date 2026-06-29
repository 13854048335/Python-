# 字面量的写法
print(100) # 整数(int)
print(3.14) # 浮点数/小数(float)
print(True) # 布尔(bool)
print(False) # 布尔(bool)
print("Hello Python") # 字符串(str)
print("-----------------") # 字符串(str)
print(None) # 空值(NoneType)

#布尔类型本质也是整数类型
print(True + 1)
print(False - 1)
print("-----------------")
# 变量 ---> Python是动态类型语言, 一个变量是可以存储不同类型的数据的 (但是项目开发中, 推荐变量只存储一种类型的数据)
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)
# 案例
# base = 20.7 # 基础播放量
# incr = 50 # 每一个月的新增播放量
# #未来两个月的播放量
# print("未来一个月的播放量:", base + incr)
# print("未来两个月的播放量:", base + incr + incr )

#一次性定义多个变量
base, incr = 20.7, 50
print("未来一个月的播放量:", base + incr)
print("未来两个月的播放量:", base + incr + incr )

# 标识符
true = 1
print(true)

name6 = "python"
print(name6)

a = 100
b = 200
c = 300

tmp = a
a = b
b = c
c = tmp

print(c,a,b)

