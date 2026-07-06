# 记账工具类
class Ledger:
    def __init__(self):
        self.records = []
        self.balance = 0 # 余额
    # 添加收入
    def add_income(self):
        income = float(input("请输入收入金额: "))
        category = input("请输入类型: ")
        note = input("请输入备注: ")
        record = {
            "amount_type": "income",
            "amount": income,
            "category": category,
            "note": note,
        }
        self.records.append(record)
        self.balance += income
        print("收入添加成功")
    # 添加支出
    def add_expense(self):
        if self.balance > 0:
            expense = float(input("请输入支出金额: "))
            category = input("请输入类型: ")
            note = input("请输入备注: ")
            record = {
                "amount_type": "expense",
                "amount": expense,
                "category": category,
                "note": note,
            }
            self.records.append(record)
            self.balance -= expense
            print("支出添加成功")
        else:
            print("余额为0不能添加支出!")
    # 查看记录
    def view_records(self):
        if not self.records:
            print("暂无记录")
            return
        for record in self.records:
            if record['amount_type'] == "income":
                print(f"收入：{record['amount']}, 类型：{record['category']}, 备注：{record['note']}")
            if record['amount_type'] == "expense":
                print(f"支出：{record['amount']}, 类型：{record['category']}, 备注：{record['note']}")

    # 查看统计
    def view_statistics(self):
        total_income = sum(r["amount"] for r in self.records if r["amount_type"] == "income")
        total_expense = sum(r["amount"] for r in self.records if r["amount_type"] == "expense")
        print("【财务统计】")
        print(f"📈 总收入: {total_income:.2f}元")
        print(f"📉 总支出: {total_expense:.2f}元")
        print(f"💰 当前余额: {self.balance:.2f}元")
    def run(self):
        while True:
            print()
            print("1.添加收入, 2.添加支出, 3.查看记录, 4.查看统计, 5.退出")
            choice = input("请选择要进行的操作（1-5）：")
            try:
                match choice:
                    case "1":
                        self.add_income()
                    case "2":
                        self.add_expense()
                    case "3":
                        self.view_records()
                    case "4":
                        self.view_statistics()
                    case "5":
                        print("感谢使用记账小程序，再见！")
                        break
                    case _:
                        print("选择的操作不合法")
            except ValueError:
                print("数据不合法，请重新输入！")
if __name__ == "__main__":
    Ledger = Ledger()
    Ledger.run()





