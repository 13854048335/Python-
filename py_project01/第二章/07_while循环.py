# while 循环 : 打印10遍 "人生苦短, 我用Python~"
i = 0
while i < 10:
    print("人生苦短, 我用Python~")
    i+=1
else:
    print("循环结束")

# while案例 : 计算1-100之间所有偶数的累加之和
total = 0
a = 1
while a < 100:
   if a % 2 == 0:
       total += a
   a += 1
print(f"1-100之间的偶数的累加之和: {total}")