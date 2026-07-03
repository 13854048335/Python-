#异常处理
try:
    print("================")
    #print(name)
    print(1 / 0)
except Exception as e:
    print("程序运行出错")
    print("异常信息",e)

