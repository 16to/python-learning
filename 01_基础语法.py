"""
Python速成教程 - 第1课：基础语法
学习内容：变量、数据类型、运算符、输入输出
"""

# ============================================
# 1. 变量和数据类型
# ============================================

print("=== 1. 变量和数据类型 ===")

# Python中不需要声明变量类型，直接赋值即可
name = "张三"  # 字符串（str）
age = 25  # 整数（int）
height = 1.75  # 浮点数（float）
is_student = True  # 布尔值（bool）

print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}米")
print(f"是否是学生：{is_student}")

# 查看变量类型
print(f"\nname的类型：{type(name)}")
print(f"age的类型：{type(age)}")
print(f"height的类型：{type(height)}")
print(f"is_student的类型：{type(is_student)}")


# ============================================
# 2. 字符串操作
# ============================================

print("\n=== 2. 字符串操作 ===")

# 字符串拼接
first_name = "李"
last_name = "明"
full_name = first_name + last_name
print(f"全名：{full_name}")

# 字符串重复
laugh = "哈" * 5
print(f"笑声：{laugh}")

# 字符串长度
message = "Hello, Python!"
print(f"消息：{message}")
print(f"消息长度：{len(message)}")

# 字符串方法
text = "  python programming  "
print(f"原始文本：'{text}'")
print(f"大写：'{text.upper()}'")
print(f"小写：'{text.lower()}'")
print(f"去除空格：'{text.strip()}'")
print(f"替换：'{text.replace('python', 'Python')}'")


# ============================================
# 3. 数字运算
# ============================================

print("\n=== 3. 数字运算 ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法：{a} + {b} = {a + b}")
print(f"减法：{a} - {b} = {a - b}")
print(f"乘法：{a} * {b} = {a * b}")
print(f"除法：{a} / {b} = {a / b}")
print(f"整除：{a} // {b} = {a // b}")
print(f"取余：{a} % {b} = {a % b}")
print(f"幂运算：{a} ** {b} = {a ** b}")

# 数学函数
import math
print(f"\n圆周率π：{math.pi}")
print(f"10的平方根：{math.sqrt(10)}")
print(f"绝对值 abs(-5)：{abs(-5)}")
print(f"四舍五入 round(3.7)：{round(3.7)}")


# ============================================
# 4. 类型转换
# ============================================

print("\n=== 4. 类型转换 ===")

# 字符串转数字
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)
print(f"字符串 '{num_str}' 转整数：{num_int}")
print(f"字符串 '{num_str}' 转浮点数：{num_float}")

# 数字转字符串
number = 42
text_number = str(number)
print(f"数字 {number} 转字符串：'{text_number}'")

# 布尔值转换
print(f"bool(1)：{bool(1)}")  # True
print(f"bool(0)：{bool(0)}")  # False
print(f"bool('')：{bool('')}")  # False（空字符串）
print(f"bool('hello')：{bool('hello')}")  # True


# ============================================
# 5. 输入输出
# ============================================

print("\n=== 5. 输入输出 ===")

# 格式化输出
name = "Python"
version = 3.11
print(f"我正在学习 {name} {version}")  # f-string（推荐）
print("我正在学习 {} {}".format(name, version))  # format方法
print("我正在学习 %s %.2f" % (name, version))  # 旧式格式化

# 用户输入（注释掉，避免阻塞执行）
# user_name = input("请输入你的名字：")
# print(f"你好，{user_name}！")

# user_age = int(input("请输入你的年龄："))
# print(f"你的年龄是：{user_age}")


# ============================================
# 6. 注释
# ============================================

print("\n=== 6. 注释 ===")

# 这是单行注释

"""
这是多行注释
可以写多行
通常用于文档说明
"""

'''
也可以用单引号
写多行注释
'''


# ============================================
# 练习题
# ============================================

print("\n=== 练习题 ===")

# 练习1：计算圆的面积和周长
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"半径为 {radius} 的圆：")
print(f"  面积 = {area:.2f}")
print(f"  周长 = {circumference:.2f}")

# 练习2：温度转换（摄氏度转华氏度）
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"\n{celsius}°C = {fahrenheit}°F")

# 练习3：字符串操作
sentence = "python is awesome"
print(f"\n原句：{sentence}")
print(f"首字母大写：{sentence.capitalize()}")
print(f"每个单词首字母大写：{sentence.title()}")
print(f"是否以'python'开头：{sentence.startswith('python')}")
print(f"是否以'awesome'结尾：{sentence.endswith('awesome')}")

print("\n✅ 第1课完成！继续学习下一课吧！")
