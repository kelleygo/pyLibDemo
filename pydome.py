import ctypes

# 加载共享对象文件
mylib = ctypes.CDLL('./pylib.so')

# 定义 Go 函数的参数和返回值类型
mylib.Add.argtypes = [ctypes.c_int, ctypes.c_int]
mylib.Add.restype = ctypes.c_int

# 调用 Go 函数
result = mylib.Add(3, 4)
print(result)  # 输出 7