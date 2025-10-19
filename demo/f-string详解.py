"""
Python字符串格式化详解
演示 f-string 的用法和对比
"""

print("=" * 50)
print("字符串格式化的三种方式对比")
print("=" * 50)

name = "小明"
age = 20
score = 95.5

# 方式1：老式 % 格式化（不推荐，老代码会见到）
print("\n【方式1：% 格式化】")
print("我叫 %s，今年 %d 岁，考了 %.1f 分" % (name, age, score))

# 方式2：.format() 方法（较新，常见）
print("\n【方式2：.format() 方法】")
print("我叫 {}，今年 {} 岁，考了 {} 分".format(name, age, score))
print("我叫 {0}，今年 {1} 岁，{0}很开心".format(name, age))  # 可以用索引

# 方式3：f-string（最推荐，Python 3.6+）
print("\n【方式3：f-string（推荐）】")
print(f"我叫 {name}，今年 {age} 岁，考了 {score} 分")

print("\n" + "=" * 50)
print("f-string 的强大功能")
print("=" * 50)

# 1. 可以直接计算表达式
print(f"\n【直接计算】")
print(f"10 + 5 = {10 + 5}")
print(f"明年我 {age + 1} 岁")
print(f"我的分数是否及格：{score >= 60}")

# 2. 可以调用函数和方法
print(f"\n【调用方法】")
print(f"大写名字：{name.upper()}")
print(f"字符串长度：{len(name)}")

# 3. 格式化数字
print(f"\n【数字格式化】")
pi = 3.14159265
print(f"圆周率：{pi}")           # 默认显示
print(f"圆周率：{pi:.2f}")       # 保留2位小数
print(f"圆周率：{pi:.4f}")       # 保留4位小数

number = 1234567
print(f"大数字：{number}")
print(f"大数字：{number:,}")      # 添加千位分隔符

# 4. 对齐和填充
print(f"\n【对齐和填充】")
print(f"左对齐：|{name:<10}|")   # < 表示左对齐，占10个字符
print(f"右对齐：|{name:>10}|")   # > 表示右对齐
print(f"居中：  |{name:^10}|")   # ^ 表示居中
print(f"填充0： |{age:05}|")     # 用0填充，总共5位

# 5. 多行 f-string
print(f"\n【多行 f-string】")
message = f"""
姓名：{name}
年龄：{age}
成绩：{score:.1f}
状态：{'及格' if score >= 60 else '不及格'}
"""
print(message)

# 6. 在循环中使用
print(f"\n【在循环中使用】")
fruits = ["苹果", "香蕉", "橙子"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. 我喜欢吃{fruit}")

# 7. 字典和对象
print(f"\n【字典】")
person = {"name": "李华", "age": 22, "city": "北京"}
print(f"{person['name']}来自{person['city']}，今年{person['age']}岁")

print("\n" + "=" * 50)
print("为什么推荐使用 f-string？")
print("=" * 50)
print("""
✅ 优点：
1. 简洁易读：直接在字符串中看到变量
2. 速度快：比其他方式更高效
3. 功能强大：可以直接写表达式
4. 不容易出错：变量名清晰可见

对比：
- 老式：print("名字：%s 年龄：%d" % (name, age))  # 容易混淆
- format：print("名字：{} 年龄：{}".format(name, age))  # 要数大括号
- f-string：print(f"名字：{name} 年龄：{age}")  # 清晰直观！
""")

print("\n" + "=" * 50)
print("实用技巧")
print("=" * 50)

# 技巧1：调试打印
print(f"\n【调试技巧】")
x = 10
y = 20
# Python 3.8+ 可以用 = 显示变量名和值
print(f"{x=}, {y=}")  # 输出：x=10, y=20

# 技巧2：日期格式化
from datetime import datetime
print(f"\n【日期格式化】")
now = datetime.now()
print(f"当前时间：{now:%Y年%m月%d日 %H:%M:%S}")

# 技巧3：百分比
print(f"\n【百分比】")
rate = 0.856
print(f"成功率：{rate:.1%}")  # 输出：85.6%

# 技巧4：科学计数法
print(f"\n【科学计数法】")
big_number = 1234567890
print(f"大数字：{big_number:e}")

print("\n✅ 记住：有 f 才能在字符串里用 {变量}！")
