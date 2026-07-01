# 案例1: 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
def triangle_area(base, height):
    """
       根据传入的底和高计算三角形面积
       :param b: 底长
       :param h: 高
       :return: 三角形面积
       """
    s = (base * height)/2
    return s
print(f"底长为3，高为2的三角形面积是：", triangle_area(3,2))

# 案例2: 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    number = 0
    for char in s:
        if char in "aeiouAEIOU":
            number += 1
    return number
print(count_aeiou("Hello Python Hello World OK"))

# 案例3: 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(score_list):
    avg = sum(score_list) / len(score_list)
    return max(score_list),min(score_list),avg
score_max,score_min,score_avg = calc_score([1,2,3,4,5])
print("最高分: ", score_max)
print("最低分: ", score_min)
print("平均分: ", score_avg)