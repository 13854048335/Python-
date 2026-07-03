class Car:
   #类属性
   wheel = 4 #轮胎数量
   tax_rate = 0.1 #购置税
   #init是初始化方法，会在对象创建时自动调用,可以在该方法中为对象设置对应的属性
   #self:表示当前所创建出来的实例对象
   #实例属性
   def __init__(self,c_color,c_brand,c_price,c_name):
      self.c_color=c_color
      self.c_brand=c_brand
      self.c_price=c_price
      self.c_name=c_name
      print("Car类型的对象初始化完毕,对象属性添加完毕")
   #魔法方法
   def __str__(self):
       return f"{self.c_color} {self.c_brand} {self.c_price} {self.c_name}"
   def __eq__(self, other):
       return self.c_name == other.c_name and self.c_color == other.c_color and self.c_price == other.c_price
   def __lt__(self, other):
       return self.c_price < other.c_price
   #定义实例方法
   def running(self):
       print(f"{self.c_brand}{self.c_name}正在高速行驶")
   def total_cost(self, discount , rate):
       """
       计算购买汽车的总费用，包含两个价格车的价格和税费
       :param discount:
       :param rate:
       :return:
       """
       total_cost = discount * self.c_price + rate * self.c_price
       return total_cost
c1 = Car("黑色","奥迪",400000,"A6")
c2 = Car("白色","奥迪",300000,"A4")
c1.running()
total = c1.total_cost(0.8,0.1)
print("提车的总费用为",total)
print(c1)
print(c1 == c2)
print(c1 < c2)
print(c1.wheel)
print(Car.wheel)
