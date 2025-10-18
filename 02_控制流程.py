"""
Python速成教程 - 第2课：控制流程
学习内容：条件语句、循环、异常处理
"""

# ============================================
# 1. 条件语句（if-elif-else）
# ============================================

print("=== 1. 条件语句 ===")

# 简单的if语句
age = 18
if age >= 18:
    print(f"年龄 {age}，已成年")

# if-else语句
score = 85
if score >= 60:
    print(f"分数 {score}，及格了！")
else:
    print(f"分数 {score}，不及格")

# if-elif-else语句
score = 88
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"分数 {score}，等级：{grade}")

# 嵌套if语句
temperature = 28
is_raining = False

if temperature > 25:
    if is_raining:
        print("天气热且下雨，带伞出门")
    else:
        print("天气热但不下雨，穿短袖")
else:
    print("天气凉爽")


# ============================================
# 2. 比较运算符和逻辑运算符
# ============================================

print("\n=== 2. 比较运算符和逻辑运算符 ===")

# 比较运算符
x = 5
y = 10
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # 等于
print(f"x != y: {x != y}")  # 不等于
print(f"x > y: {x > y}")    # 大于
print(f"x < y: {x < y}")    # 小于
print(f"x >= y: {x >= y}")  # 大于等于
print(f"x <= y: {x <= y}")  # 小于等于

# 逻辑运算符
age = 25
has_license = True
print(f"\nage = {age}, has_license = {has_license}")
print(f"age >= 18 and has_license: {age >= 18 and has_license}")  # 与
print(f"age < 18 or has_license: {age < 18 or has_license}")      # 或
print(f"not has_license: {not has_license}")                       # 非


# ============================================
# 3. for循环
# ============================================

print("\n=== 3. for循环 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("水果列表：")
for fruit in fruits:
    print(f"  - {fruit}")

# 使用range()
print("\n打印1到5：")
for i in range(1, 6):
    print(i, end=" ")
print()

# range()的三个参数：起始、结束、步长
print("\n打印0到10的偶数：")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# enumerate()获取索引和值
print("\n带索引的水果列表：")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# ============================================
# 4. while循环
# ============================================

print("\n=== 4. while循环 ===")

# 基本while循环
count = 1
print("倒计时：")
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# 带条件的while循环
number = 1
print("\n小于100的2的幂：")
while number < 100:
    print(number, end=" ")
    number *= 2
print()


# ============================================
# 5. break和continue
# ============================================

print("\n=== 5. break和continue ===")

# break：跳出整个循环
print("找到第一个能被7整除的数：")
for i in range(1, 51):
    if i % 7 == 0:
        print(f"找到了：{i}")
        break

# continue：跳过本次循环
print("\n1到10中的奇数：")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()


# ============================================
# 6. 列表推导式（List Comprehension）
# ============================================

print("\n=== 6. 列表推导式 ===")

# 传统方法
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"传统方法生成平方数：{squares}")

# 列表推导式（简洁）
squares = [i ** 2 for i in range(1, 6)]
print(f"推导式生成平方数：{squares}")

# 带条件的列表推导式
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(f"1到20的偶数：{even_numbers}")


# ============================================
# 7. 异常处理（try-except）
# ============================================

print("\n=== 7. 异常处理 ===")

# 基本异常处理
try:
    number = int("abc")  # 这会引发ValueError
except ValueError:
    print("错误：无法将字符串转换为整数")

# 处理多种异常
try:
    result = 10 / 0  # 这会引发ZeroDivisionError
except ZeroDivisionError:
    print("错误：不能除以零")
except ValueError:
    print("错误：值错误")

# try-except-else-finally
try:
    x = 10
    y = 2
    result = x / y
except ZeroDivisionError:
    print("除数不能为零")
else:
    print(f"计算成功：{x} / {y} = {result}")
finally:
    print("无论是否出错，这里都会执行")


# ============================================
# 练习题
# ============================================

print("\n=== 练习题 ===")

# 练习1：打印九九乘法表
print("\n九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()

# 练习2：判断是否为质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\n2到30之间的质数：")
primes = [i for i in range(2, 31) if is_prime(i)]
print(primes)

# 练习3：斐波那契数列
print("\n斐波那契数列（前10项）：")
fib = [0, 1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)

# 练习4：猜数字游戏（简化版）
import random
secret_number = random.randint(1, 10)
print(f"\n猜数字游戏（答案是1-10之间）")
print(f"提示：正确答案是 {secret_number}")
# 实际游戏需要用户输入，这里仅做演示
for guess in [5, 7, secret_number]:
    if guess == secret_number:
        print(f"猜 {guess}：恭喜你猜对了！")
        break
    elif guess < secret_number:
        print(f"猜 {guess}：太小了")
    else:
        print(f"猜 {guess}：太大了")

print("\n✅ 第2课完成！继续加油！")
