"""
Python能力评估测试
完成这些测试来证明你已经掌握了Python！
"""

print("="*60)
print("Python能力评估测试".center(60))
print("="*60)
print("\n请完成以下编程任务来证明你的Python能力！\n")

# ============================================
# 测试1：基础语法 (10分)
# ============================================

print("【测试1：基础语法】(10分)")
print("任务：创建变量并进行运算")
print("-" * 50)

# TODO: 完成以下任务
# 1. 创建三个变量：name(你的名字), age(你的年龄), height(你的身高)
# 2. 计算10年后你的年龄
# 3. 使用f-string打印："{name}，10年后你将{future_age}岁"

# 在这里写你的代码：
# name = 
# age = 
# height = 
# future_age = 
# print(...)

print("\n✓ 完成测试1后，运行代码查看结果\n")


# ============================================
# 测试2：控制流程 (15分)
# ============================================

print("【测试2：控制流程】(15分)")
print("任务：实现FizzBuzz游戏")
print("-" * 50)
print("规则：")
print("  - 如果数字能被3整除，输出'Fizz'")
print("  - 如果数字能被5整除，输出'Buzz'")
print("  - 如果数字同时能被3和5整除，输出'FizzBuzz'")
print("  - 否则输出数字本身")

# TODO: 实现FizzBuzz函数
def fizzbuzz(n):
    """
    参数: n - 整数
    返回: 根据规则返回字符串或数字
    """
    # 在这里写你的代码
    pass

# 测试你的函数
print("\n测试FizzBuzz:")
for i in range(1, 16):
    result = fizzbuzz(i)
    if result:  # 如果你实现了函数
        print(f"{i}: {result}")

print("\n✓ 完成测试2后，运行代码查看结果\n")


# ============================================
# 测试3：函数 (15分)
# ============================================

print("【测试3：函数】(15分)")
print("任务：实现一个回文检测函数")
print("-" * 50)

# TODO: 实现回文检测函数
def is_palindrome(text):
    """
    检测一个字符串是否是回文
    参数: text - 字符串
    返回: True或False
    提示: 忽略大小写和空格
    """
    # 在这里写你的代码
    pass

# 测试用例
test_cases = [
    "aba",
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw"
]

print("\n测试回文检测:")
for text in test_cases:
    result = is_palindrome(text)
    if result is not None:  # 如果你实现了函数
        print(f"'{text}' -> {result}")

print("\n✓ 完成测试3后，运行代码查看结果\n")


# ============================================
# 测试4：数据结构 (20分)
# ============================================

print("【测试4：数据结构】(20分)")
print("任务：分析学生成绩数据")
print("-" * 50)

students_data = [
    {"name": "Alice", "scores": [85, 90, 88]},
    {"name": "Bob", "scores": [92, 88, 95]},
    {"name": "Charlie", "scores": [78, 85, 80]},
    {"name": "David", "scores": [95, 92, 98]},
]

# TODO: 完成以下任务
# 1. 计算每个学生的平均分
# 2. 找出平均分最高的学生
# 3. 计算全班的平均分
# 4. 统计有多少学生平均分在90分以上

# 在这里写你的代码：
def analyze_scores(students):
    """
    分析学生成绩
    返回: 包含分析结果的字典
    """
    # 在这里写你的代码
    pass

# 调用函数并打印结果
# result = analyze_scores(students_data)
# if result:
#     print(f"平均分最高的学生: {result.get('top_student')}")
#     print(f"全班平均分: {result.get('class_average'):.2f}")
#     print(f"90分以上人数: {result.get('high_achievers')}")

print("\n✓ 完成测试4后，运行代码查看结果\n")


# ============================================
# 测试5：面向对象 (20分)
# ============================================

print("【测试5：面向对象】(20分)")
print("任务：实现一个银行账户类")
print("-" * 50)

# TODO: 实现BankAccount类
class BankAccount:
    """
    银行账户类
    
    要求：
    1. 初始化时需要账户名和初始余额（默认0）
    2. 实现存款方法deposit(amount)
    3. 实现取款方法withdraw(amount)，余额不足时返回False
    4. 实现获取余额方法get_balance()
    5. 实现__str__方法，返回"账户：{name}，余额：{balance}元"
    """
    
    def __init__(self, name, balance=0):
        # 在这里写你的代码
        pass
    
    def deposit(self, amount):
        # 在这里写你的代码
        pass
    
    def withdraw(self, amount):
        # 在这里写你的代码
        pass
    
    def get_balance(self):
        # 在这里写你的代码
        pass
    
    def __str__(self):
        # 在这里写你的代码
        pass

# 测试你的类
print("\n测试银行账户类:")
# account = BankAccount("张三", 1000)
# print(account)
# account.deposit(500)
# print(account)
# account.withdraw(300)
# print(account)
# success = account.withdraw(2000)
# print(f"取款2000元: {'成功' if success else '失败'}")

print("\n✓ 完成测试5后，运行代码查看结果\n")


# ============================================
# 测试6：综合实战 (20分)
# ============================================

print("【测试6：综合实战】(20分)")
print("任务：实现一个待办事项管理器")
print("-" * 50)

# TODO: 实现TodoList类
class TodoList:
    """
    待办事项管理器
    
    要求：
    1. 初始化一个空的待办列表
    2. add_task(task): 添加任务
    3. complete_task(index): 标记任务为完成
    4. remove_task(index): 删除任务
    5. show_tasks(): 显示所有任务（标记完成状态）
    6. get_pending_count(): 返回未完成任务数量
    """
    
    def __init__(self):
        # 在这里写你的代码
        pass
    
    def add_task(self, task):
        # 在这里写你的代码
        pass
    
    def complete_task(self, index):
        # 在这里写你的代码
        pass
    
    def remove_task(self, index):
        # 在这里写你的代码
        pass
    
    def show_tasks(self):
        # 在这里写你的代码
        pass
    
    def get_pending_count(self):
        # 在这里写你的代码
        pass

# 测试你的类
print("\n测试待办事项管理器:")
# todo = TodoList()
# todo.add_task("学习Python基础")
# todo.add_task("完成练习题")
# todo.add_task("做实战项目")
# todo.show_tasks()
# todo.complete_task(0)
# todo.show_tasks()
# print(f"未完成任务数: {todo.get_pending_count()}")

print("\n✓ 完成测试6后，运行代码查看结果\n")


# ============================================
# 评分标准
# ============================================

print("\n" + "="*60)
print("评分标准".center(60))
print("="*60)
print("""
测试1：基础语法 (10分)
  - 正确创建变量并进行运算

测试2：控制流程 (15分)
  - 正确实现FizzBuzz逻辑
  - 使用if-elif-else或其他方法

测试3：函数 (15分)
  - 正确处理回文判断
  - 正确处理大小写和空格

测试4：数据结构 (20分)
  - 正确使用列表和字典
  - 正确计算统计数据

测试5：面向对象 (20分)
  - 正确定义类和方法
  - 实现封装和数据验证

测试6：综合实战 (20分)
  - 综合运用所学知识
  - 代码结构清晰

总分：100分

等级划分：
  90-100分：优秀 - 你已经掌握了Python！🎉
  80-89分：良好 - 再加把劲就能精通了！💪
  70-79分：中等 - 继续学习和练习！📚
  60-69分：及格 - 需要复习基础知识！🔄
  60分以下：需要重新学习 - 不要气馁，继续努力！💪
""")

print("\n" + "="*60)
print("提示：完成所有测试后，可以对照答案文件检查！".center(60))
print("="*60)
