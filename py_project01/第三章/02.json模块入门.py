# 写入json数据文件
import json
data = {"name": "张三", "age": 18}
with open("resources/user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# 读取json文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
