"""
Python速成教程 - 第3课：函数和模块
学习内容：函数定义、参数、返回值、作用域、模块导入
"""

# ============================================
# 1. 函数基础
# ============================================

print("=== 1. 函数基础 ===")

# 定义一个简单的函数
def greet():
    """这是一个简单的问候函数"""
    print("你好，欢迎学习Python！")

# 调用函数
greet()


# 带参数的函数
def greet_person(name):
    """问候指定的人"""
    print(f"你好，{name}！")

greet_person("小明")
greet_person("小红")


# 带返回值的函数
def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")


# ============================================
# 2. 函数参数
# ============================================

print("\n=== 2. 函数参数 ===")

# 默认参数
def power(base, exponent=2):
    """计算幂，默认是平方"""
    return base ** exponent

print(f"2的平方：{power(2)}")
print(f"2的立方：{power(2, 3)}")
print(f"3的4次方：{power(3, 4)}")


# 关键字参数
def introduce(name, age, city):
    """自我介绍"""
    print(f"我叫{name}，{age}岁，来自{city}")

introduce(name="张三", age=25, city="北京")
introduce(age=30, city="上海", name="李四")  # 顺序可以不同


# 可变参数 *args
def sum_all(*numbers):
    """计算所有数字的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# 关键字可变参数 **kwargs
def print_info(**info):
    """打印所有键值对信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n学生信息：")
print_info(name="王五", age=20, major="计算机科学", gpa=3.8)


# 混合使用参数
def complex_function(a, b, *args, option=None, **kwargs):
    """演示各种参数类型"""
    print(f"位置参数：a={a}, b={b}")
    print(f"可变参数：args={args}")
    print(f"默认参数：option={option}")
    print(f"关键字参数：kwargs={kwargs}")

print("\n复杂函数调用：")
complex_function(1, 2, 3, 4, 5, option="test", x=10, y=20)


# ============================================
# 3. Lambda表达式（匿名函数）
# ============================================

print("\n=== 3. Lambda表达式 ===")

# 普通函数
def square(x):
    return x ** 2

# Lambda表达式（等价）
square_lambda = lambda x: x ** 2

print(f"普通函数 square(5) = {square(5)}")
print(f"Lambda表达式 square_lambda(5) = {square_lambda(5)}")

# Lambda在排序中的应用
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("\n按分数排序：")
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")


# ============================================
# 4. 变量作用域
# ============================================

print("\n=== 4. 变量作用域 ===")

# 全局变量
global_var = "我是全局变量"

def test_scope():
    # 局部变量
    local_var = "我是局部变量"
    print(f"函数内部 - global_var: {global_var}")
    print(f"函数内部 - local_var: {local_var}")

test_scope()
print(f"函数外部 - global_var: {global_var}")
# print(local_var)  # 这会报错，因为local_var在函数外不可访问


# 修改全局变量
counter = 0

def increment():
    global counter  # 声明使用全局变量
    counter += 1
    print(f"Counter: {counter}")

increment()
increment()
increment()


# ============================================
# 5. 内置函数
# ============================================

print("\n=== 5. 常用内置函数 ===")

# 数值函数
numbers = [1, 5, 3, 9, 2, 7]
print(f"列表：{numbers}")
print(f"max(): {max(numbers)}")
print(f"min(): {min(numbers)}")
print(f"sum(): {sum(numbers)}")
print(f"len(): {len(numbers)}")

# map()：对每个元素应用函数
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nmap() 平方：{squared}")

# filter()：过滤元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter() 偶数：{evens}")

# zip()：打包多个列表
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print(f"\nzip() 组合：{combined}")

# enumerate()：添加索引
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")


# ============================================
# 6. 递归函数
# ============================================

print("\n=== 6. 递归函数 ===")

# 阶乘
def factorial(n):
    """计算n的阶乘"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"5的阶乘：{factorial(5)}")

# 斐波那契数列
def fibonacci(n):
    """返回第n个斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"斐波那契数列前10项：{[fibonacci(i) for i in range(10)]}")


# ============================================
# 7. 文档字符串和类型提示
# ============================================

print("\n=== 7. 文档字符串和类型提示 ===")

def calculate_area(length: float, width: float) -> float:
    """
    计算矩形面积
    
    参数:
        length: 长度
        width: 宽度
    
    返回:
        矩形面积
    """
    return length * width

area = calculate_area(5.0, 3.0)
print(f"矩形面积：{area}")

# 查看文档字符串
print(f"\n函数文档：\n{calculate_area.__doc__}")


# ============================================
# 练习题
# ============================================

print("\n=== 练习题 ===")

# 练习1：判断回文数
def is_palindrome(n):
    """判断一个数是否是回文数"""
    s = str(n)
    return s == s[::-1]

print("\n回文数测试：")
for num in [121, 123, 1221, 12321]:
    print(f"{num} 是回文数：{is_palindrome(num)}")


# 练习2：列表去重
def remove_duplicates(lst):
    """去除列表中的重复元素"""
    return list(set(lst))

original = [1, 2, 2, 3, 4, 4, 5, 1]
unique = remove_duplicates(original)
print(f"\n原列表：{original}")
print(f"去重后：{unique}")


# 练习3：统计字符串中各字符出现次数
def count_characters(text):
    """统计字符出现次数"""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

text = "hello world"
char_counts = count_characters(text)
print(f"\n'{text}' 字符统计：")
for char, count in sorted(char_counts.items()):
    if char != ' ':
        print(f"  '{char}': {count}")


# 练习4：实现简单的计算器
def calculator(a, b, operation):
    """简单计算器"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "除数不能为0"
    }
    return operations.get(operation, lambda x, y: "未知操作")(a, b)

print("\n计算器测试：")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")

print("\n✅ 第3课完成！函数是编程的核心！")
