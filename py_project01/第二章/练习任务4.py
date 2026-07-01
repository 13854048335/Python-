"""
函数练习
需求：实现各种实用函数
思路：1) 实现计算函数（加减乘除）2) 实现字符串处理函数 3) 使用lambda简化代码
"""
#加
def add (x, y):
    al = x + y
    return al
# 减
def subtract(x, y):
    al = x - y
    return al
# 乘
def multiply(x, y):
    al = x * y
    return al
# 除
def divide(x, y):
    al = x / y
    return al
#字符串处理函数
def clean(text):
    """清理空格"""
    return ' '.join(str(text).strip().split())

def get_digits(text):
    """提取数字"""
    return ''.join(c for c in str(text) if c.isdigit())

# 使用
print(clean("  hello   world  "))      # hello world      # 138****5678
print(get_digits("价格199.99元"))       # 19999
#使用lambda简化代码
add = lambda x, y: x + y
sub = lambda x, y: x - y
multi = lambda x, y: x * y
divide = lambda x, y: x / y