"""
Python速成教程 - 第4课：数据结构
学习内容：列表、元组、字典、集合
"""

# ============================================
# 1. 列表（List）
# ============================================

print("=== 1. 列表（List）===")

# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"水果列表：{fruits}")
print(f"数字列表：{numbers}")
print(f"混合列表：{mixed}")

# 访问元素
print(f"\n第一个水果：{fruits[0]}")
print(f"最后一个水果：{fruits[-1]}")
print(f"前三个水果：{fruits[:3]}")
print(f"后两个水果：{fruits[-2:]}")

# 修改元素
fruits[1] = "草莓"
print(f"修改后的列表：{fruits}")

# 列表方法
print("\n列表操作：")
fruits.append("西瓜")  # 末尾添加
print(f"append('西瓜')：{fruits}")

fruits.insert(1, "芒果")  # 指定位置插入
print(f"insert(1, '芒果')：{fruits}")

fruits.remove("橙子")  # 删除指定元素
print(f"remove('橙子')：{fruits}")

popped = fruits.pop()  # 删除并返回最后一个元素
print(f"pop()删除：{popped}，剩余：{fruits}")

fruits.sort()  # 排序
print(f"sort()排序：{fruits}")

fruits.reverse()  # 反转
print(f"reverse()反转：{fruits}")

# 列表拷贝
fruits_copy = fruits.copy()
fruits_copy.append("榴莲")
print(f"\n原列表：{fruits}")
print(f"拷贝列表：{fruits_copy}")

# 列表推导式
squares = [x**2 for x in range(1, 11)]
print(f"\n1-10的平方：{squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"1-10中偶数的平方：{even_squares}")


# ============================================
# 2. 元组（Tuple）
# ============================================

print("\n=== 2. 元组（Tuple）===")

# 创建元组（不可变）
point = (3, 5)
rgb = (255, 128, 0)
single = (42,)  # 单元素元组需要逗号

print(f"坐标点：{point}")
print(f"RGB颜色：{rgb}")
print(f"单元素元组：{single}")

# 访问元素
print(f"\nx坐标：{point[0]}")
print(f"y坐标：{point[1]}")

# 元组解包
x, y = point
print(f"解包后：x={x}, y={y}")

r, g, b = rgb
print(f"RGB：红={r}，绿={g}，蓝={b}")

# 元组的不可变性
# point[0] = 10  # 这会报错！元组不能修改

# 元组可以作为字典的键（列表不行）
locations = {
    (0, 0): "原点",
    (1, 0): "右侧",
    (0, 1): "上方"
}
print(f"\n位置映射：{locations}")


# ============================================
# 3. 字典（Dictionary）
# ============================================

print("\n=== 3. 字典（Dictionary）===")

# 创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "skills": ["Python", "Java", "SQL"]
}

print(f"个人信息：{person}")

# 访问元素
print(f"\n姓名：{person['name']}")
print(f"年龄：{person.get('age')}")
print(f"国籍：{person.get('country', '未知')}")  # 提供默认值

# 修改和添加
person["age"] = 26
person["email"] = "zhangsan@example.com"
print(f"\n更新后：{person}")

# 删除元素
del person["city"]
print(f"删除city后：{person}")

# 字典方法
print("\n字典方法：")
print(f"所有键：{list(person.keys())}")
print(f"所有值：{list(person.values())}")
print(f"所有键值对：{list(person.items())}")

# 遍历字典
print("\n遍历字典：")
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(f"\n数字平方字典：{square_dict}")

# 嵌套字典
students = {
    "S001": {"name": "Alice", "score": 85},
    "S002": {"name": "Bob", "score": 92},
    "S003": {"name": "Charlie", "score": 78}
}
print(f"\n学生信息：")
for sid, info in students.items():
    print(f"{sid}: {info['name']} - {info['score']}分")


# ============================================
# 4. 集合（Set）
# ============================================

print("\n=== 4. 集合（Set）===")

# 创建集合（无序、不重复）
colors = {"红", "绿", "蓝"}
numbers_set = {1, 2, 3, 4, 5}

print(f"颜色集合：{colors}")
print(f"数字集合：{numbers_set}")

# 从列表创建集合（自动去重）
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(f"\n原列表：{numbers_list}")
print(f"去重后集合：{unique_numbers}")

# 集合操作
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"\nset_a: {set_a}")
print(f"set_b: {set_b}")
print(f"并集：{set_a | set_b}")
print(f"交集：{set_a & set_b}")
print(f"差集（a-b）：{set_a - set_b}")
print(f"对称差集：{set_a ^ set_b}")

# 集合方法
colors.add("黄")
print(f"\nadd('黄')：{colors}")

colors.remove("红")
print(f"remove('红')：{colors}")

# 判断成员
print(f"'绿' in colors: {'绿' in colors}")
print(f"'红' in colors: {'红' in colors}")


# ============================================
# 5. 数据结构选择指南
# ============================================

print("\n=== 5. 数据结构选择指南 ===")
print("""
列表（List）：
  - 有序、可变、可重复
  - 适合：需要保持顺序、频繁修改的场景
  - 例如：待办事项、成绩列表

元组（Tuple）：
  - 有序、不可变、可重复
  - 适合：不需要修改的数据、作为字典键
  - 例如：坐标点、配置常量

字典（Dictionary）：
  - 无序、键值对、键唯一
  - 适合：需要快速查找、映射关系
  - 例如：用户信息、配置项

集合（Set）：
  - 无序、不重复
  - 适合：去重、集合运算
  - 例如：标签、权限集合
""")


# ============================================
# 练习题
# ============================================

print("=== 练习题 ===")

# 练习1：合并两个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print(f"\n字典合并：")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"合并后: {merged}")

# 练习2：找出两个列表的公共元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"\nlist1: {list1}")
print(f"list2: {list2}")
print(f"公共元素: {common}")

# 练习3：词频统计
text = "python is great and python is easy to learn"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"\n文本: '{text}'")
print(f"词频统计:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# 练习4：矩阵转置
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"\n原矩阵:")
for row in matrix:
    print(f"  {row}")
print(f"转置后:")
for row in transposed:
    print(f"  {row}")

# 练习5：学生成绩管理
students_scores = {
    "Alice": [85, 90, 88],
    "Bob": [92, 88, 95],
    "Charlie": [78, 85, 80]
}

print(f"\n学生成绩分析:")
for name, scores in students_scores.items():
    average = sum(scores) / len(scores)
    print(f"{name}: 成绩={scores}, 平均分={average:.2f}")

print("\n✅ 第4课完成！数据结构是编程的基石！")
