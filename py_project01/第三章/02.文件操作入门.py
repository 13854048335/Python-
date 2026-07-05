# 读文件
# 打开文件
f = open("resources/测试.txt", "r", encoding="utf-8")

# 读取文件内容
# content = f.read()
# print(content)
content = f.readlines()
for line in content:
    print(line.strip(), end='')
# 关闭文件
f.close()

# 写入文件
#
with open("resources/测试.txt", "w", encoding="utf-8") as f:
    # 2. 写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")

import datetime

print(datetime.datetime.now())
