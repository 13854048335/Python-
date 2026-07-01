def print_hello():
    print("hello")
print_hello()
# 计算圆的面积
def circleArea(r):
    s = 3.14*r**2
    return s

area = circleArea(5)
print(f"圆的面积为{area}")

# 函数3: 计算圆的面积, 周长 -- 半径 ----> 如果返回值有多个, 多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """
    #     根据圆的半径, 计算圆的面积和周长
    #     :param r: 半径
    #     :return: 圆的面积, 圆的周长
    #     """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
area, length = circle_area_len(10) # 解包
print(area)
print(length)

# 函数嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()

print("函数调用完毕 ~")