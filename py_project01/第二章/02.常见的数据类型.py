# 常见数据类型 ---> type() 获取指定的字面量或变量的类型
from email import message
from math import hypot

print("Hello Python")
print(type("Hello Python"))

print(type(10))
print(type(1.34))
print(type(True))
print(type(False))
print(type(None))
num = -100
print(type(num))
# # 常见数据类型 ---> isinstance(数据, 类型) --> bool值 --> 判定数据是否是指定的类型, 如果是: True, 否则: False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))

#字符串
# s1 = "Python"
# s2 = 'Hello Python'
# s3 = """
#     Hello:
#      欢迎大家进入到Python课程的学习!
#      大家记得一键三连哦 ~
# """   # 三引号定义 (多行字符串)
# print(s1)
# print(s2)
# print(s3)

msg = 'It\'s very good'
print(msg)
print(type(msg))
msg2 = "It's very good"
print(msg2)

msg3 = "Hello 的意思就是 \"您好\""
print(msg3)

msg4 = 'Hello 的意思就是 \"您好\"'
print(msg4)

print("\t欢迎大家进入到Python课程的学习!\n\t大家记得一键三连哦 ~")

s1 = "人生苦短"  "我学Python"
print(s1)
msg1 = "人生苦短"
msg2 = "我学Python"
s2 = msg1 + msg2
print(s2)

name = '涛哥'
age = 20
Professional = "软件工程"
Hobby = "Python、Java"
print("大家好，我的名字叫：%s 今年 %s 岁，学习的专业是%s，爱好是%s" % (name,age,Professional,Hobby))
print(f"大家好，我的名字叫{name} 今年{age}岁，学习的专业是{Professional}，爱好是{Hobby}")


