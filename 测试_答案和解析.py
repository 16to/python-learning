"""
Python能力评估测试 - 参考答案
完成测试后可以对照这个文件检查你的答案
"""

print("="*60)
print("Python能力评估测试 - 参考答案".center(60))
print("="*60)

# ============================================
# 测试1：基础语法 - 参考答案
# ============================================

print("\n【测试1：基础语法 - 参考答案】")
print("-" * 50)

# 答案
name = "小明"
age = 20
height = 1.75
future_age = age + 10
print(f"{name}，10年后你将{future_age}岁")

print("\n解析：")
print("  - 创建变量直接赋值即可")
print("  - 使用f-string格式化输出：f'{变量}'")
print("  - 注意变量命名规范（小写，下划线分隔）")


# ============================================
# 测试2：控制流程 - 参考答案
# ============================================

print("\n\n【测试2：控制流程 - 参考答案】")
print("-" * 50)

# 方法1：标准if-elif-else
def fizzbuzz_v1(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

# 方法2：字符串拼接（更优雅）
def fizzbuzz_v2(n):
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result if result else n

print("方法1测试：")
for i in range(1, 16):
    print(f"{i}: {fizzbuzz_v1(i)}")

print("\n解析：")
print("  - 使用 % 运算符检查整除")
print("  - 注意先判断同时被3和5整除的情况")
print("  - 方法2更简洁，避免了重复判断")


# ============================================
# 测试3：函数 - 参考答案
# ============================================

print("\n\n【测试3：函数 - 参考答案】")
print("-" * 50)

# 方法1：基础版本
def is_palindrome_v1(text):
    # 转为小写并去除空格
    clean_text = text.lower().replace(" ", "")
    # 比较字符串和它的反转
    return clean_text == clean_text[::-1]

# 方法2：只保留字母
def is_palindrome_v2(text):
    # 只保留字母并转小写
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

test_cases = [
    "aba",
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw"
]

print("测试结果：")
for text in test_cases:
    result = is_palindrome_v2(text)
    print(f"'{text}' -> {result}")

print("\n解析：")
print("  - 使用lower()转小写")
print("  - 使用replace(' ', '')或isalnum()去除空格/标点")
print("  - 使用[::-1]反转字符串")
print("  - 注意要处理标点符号和大小写")


# ============================================
# 测试4：数据结构 - 参考答案
# ============================================

print("\n\n【测试4：数据结构 - 参考答案】")
print("-" * 50)

students_data = [
    {"name": "Alice", "scores": [85, 90, 88]},
    {"name": "Bob", "scores": [92, 88, 95]},
    {"name": "Charlie", "scores": [78, 85, 80]},
    {"name": "David", "scores": [95, 92, 98]},
]

def analyze_scores(students):
    # 计算每个学生的平均分
    for student in students:
        student['average'] = sum(student['scores']) / len(student['scores'])
    
    # 找出平均分最高的学生
    top_student = max(students, key=lambda s: s['average'])
    
    # 计算全班平均分
    class_average = sum(s['average'] for s in students) / len(students)
    
    # 统计90分以上人数
    high_achievers = sum(1 for s in students if s['average'] >= 90)
    
    return {
        'top_student': f"{top_student['name']} ({top_student['average']:.2f}分)",
        'class_average': class_average,
        'high_achievers': high_achievers
    }

result = analyze_scores(students_data)
print("分析结果：")
print(f"  平均分最高的学生: {result['top_student']}")
print(f"  全班平均分: {result['class_average']:.2f}")
print(f"  90分以上人数: {result['high_achievers']}")

print("\n解析：")
print("  - 使用sum()和len()计算平均分")
print("  - 使用max()和lambda找最大值")
print("  - 使用生成器表达式进行统计")
print("  - 使用字典存储结构化数据")


# ============================================
# 测试5：面向对象 - 参考答案
# ============================================

print("\n\n【测试5：面向对象 - 参考答案】")
print("-" * 50)

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # 私有属性
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"账户：{self.name}，余额：{self.__balance}元"

print("测试银行账户类:")
account = BankAccount("张三", 1000)
print(account)
account.deposit(500)
print(f"存款500元后: {account}")
account.withdraw(300)
print(f"取款300元后: {account}")
success = account.withdraw(2000)
print(f"取款2000元: {'成功' if success else '失败（余额不足）'}")

print("\n解析：")
print("  - 使用__init__初始化属性")
print("  - 使用双下划线__创建私有属性")
print("  - 在方法中进行数据验证")
print("  - 实现__str__方法自定义打印格式")


# ============================================
# 测试6：综合实战 - 参考答案
# ============================================

print("\n\n【测试6：综合实战 - 参考答案】")
print("-" * 50)

class TodoList:
    def __init__(self):
        self.tasks = []  # 每个任务是一个字典：{"task": "...", "completed": False}
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"✓ 已添加任务：{task}")
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"✓ 已完成任务：{self.tasks[index]['task']}")
            return True
        print("✗ 无效的任务索引")
        return False
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"✓ 已删除任务：{removed['task']}")
            return True
        print("✗ 无效的任务索引")
        return False
    
    def show_tasks(self):
        if not self.tasks:
            print("暂无任务")
            return
        
        print("\n待办任务列表：")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            print(f"  {i}. [{status}] {task['task']}")
    
    def get_pending_count(self):
        return sum(1 for task in self.tasks if not task["completed"])

print("测试待办事项管理器:")
todo = TodoList()
todo.add_task("学习Python基础")
todo.add_task("完成练习题")
todo.add_task("做实战项目")
todo.show_tasks()
print("\n标记第一个任务为完成：")
todo.complete_task(0)
todo.show_tasks()
print(f"\n未完成任务数: {todo.get_pending_count()}")

print("\n解析：")
print("  - 使用列表存储任务，每个任务是一个字典")
print("  - 字典包含task（任务内容）和completed（完成状态）")
print("  - 使用索引访问和修改任务")
print("  - 使用生成器表达式统计未完成任务")


# ============================================
# 总结和建议
# ============================================

print("\n\n" + "="*60)
print("学习建议".center(60))
print("="*60)
print("""
如果你能独立完成这些测试，说明你已经掌握了Python基础！

下一步学习方向：

1. 深入学习（推荐）
   - 文件操作（读写文件）
   - 正则表达式（文本处理）
   - 装饰器和生成器（高级特性）
   - 多线程和异步编程

2. 实战项目
   - 开发一个完整的Web应用
   - 数据分析项目
   - 自动化脚本
   - API开发

3. 学习框架
   - Web: Flask/Django/FastAPI
   - 数据: Pandas/NumPy
   - 机器学习: Scikit-learn/TensorFlow

记住：
  - 编程是实践性技能，多写代码才能提高
  - 遇到问题先自己思考，再查文档/搜索
  - 参与开源项目，阅读优秀代码
  - 持续学习，保持好奇心

祝你编程之路越走越远！🚀
""")
