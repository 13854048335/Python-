# 极简版待办事项管理
tasks = []

while True:
    print("\n1. 添加  2. 删除  3. 查看  4. 退出")
    choice = input("请选择: ")

    if choice == "1":
        task = input("输入待办事项: ")
        if task.strip() != "":
            tasks.append(task)
            print(f"已添加: {task}")
        else:
            print("内容不能为空！")

    elif choice == "2":
        if len(tasks) == 0:
            print("暂无待办事项！")
        else:
            # 显示所有任务
            print("\n当前待办事项：")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i = i + 1

            index_str = input("请输入要删除的编号: ")
            if index_str.isdigit():
                index = int(index_str)
                if 1 <= index <= len(tasks):
                    deleted = tasks.pop(index - 1)
                    print(f"已删除: {deleted}")
                else:
                    print("编号超出范围！")
            else:
                print("请输入数字！")

    elif choice == "3":
        if len(tasks) == 0:
            print("暂无待办事项！")
        else:
            print("\n当前待办事项：")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i = i + 1

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效选项！")