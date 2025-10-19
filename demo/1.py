# 变量和类型
print("Hello, World!")

name = "张三"

print(f"姓名：{name}")

print(f"类型{type(name)}") # f是格式化字符串用

# 字符串操作

first_name = "李"
last_name = "四"

## 字符串拼接
full_name = first_name + last_name
print(full_name)

## 字符串长度
print(len(full_name))

## 字符串方法
text = "  python 编程  "
print(text.upper()) # 大写
print(text.lower()) # 小写
print(text.strip()) # 去除空格
print(text.replace("python", "Python")) # 替换

# 数字运算
a = 10
b = 3
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}") # 整除
print(f"a % b = {a % b}")   # 取余
print(f"a ** b = {a ** b}") # 幂运算，10的3次方

import math
print(f"math.sqrt(16) = {math.sqrt(16)}") # 平方根
print(f"math.pi = {math.pi}")             # 圆周率π
print(f"math.round(3.6) = {math.round(3.6)}") # 四舍五入
print(f"math.abs(-5) = {math.abs(-5)}")       # 绝对值
print(f"math.ceil(3.2) = {math.ceil(3.2)}")   # 向上取整
print(f"math.floor(3.8) = {math.floor(3.8)}") # 向下取整

# 类型转换
num_str = "123"
num_int = int(num_str)   # 字符串转整数
num_float = float(num_str) # 字符串转浮点数
print(f"num_int + 10 = {num_int + 10}")
print(f"num_float + 0.5 = {num_float + 0.5}")
num = 36
text = str(num) # 数字转字符串
print(text) # 输出字符串"36"
print(f"bool(0) = {bool(0)}") # 转为布尔值False
print(f"bool(1) = {bool(1)}") # 转为布尔值True
print(f"bool('') = {bool('')}") # 转为布尔值False
print(f"bool('abc') = {bool('abc')}") # 转为布尔值True

# 输入和输出
user_name = input("请输入你的名字：")
print(f"你好，{user_name}！")

# 注释

"""
多行注释可以使用三个引号
"""
# 这是单行注释

