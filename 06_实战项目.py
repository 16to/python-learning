"""
Python速成教程 - 第6课：实战项目
综合应用所学知识的实际项目
"""

import random
import json
from datetime import datetime

# ============================================
# 项目1：待办事项管理器
# ============================================

print("=== 项目1：待办事项管理器 ===\n")

class TodoItem:
    """待办事项"""
    
    def __init__(self, title, description="", priority="中"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def mark_complete(self):
        """标记为完成"""
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title} (优先级:{self.priority})"

class TodoList:
    """待办事项列表"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, title, description="", priority="中"):
        """添加事项"""
        item = TodoItem(title, description, priority)
        self.items.append(item)
        print(f"已添加：{title}")
    
    def complete_item(self, index):
        """完成事项"""
        if 0 <= index < len(self.items):
            self.items[index].mark_complete()
            print(f"已完成：{self.items[index].title}")
        else:
            print("无效的索引")
    
    def remove_item(self, index):
        """删除事项"""
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"已删除：{removed.title}")
        else:
            print("无效的索引")
    
    def list_all(self):
        """显示所有事项"""
        if not self.items:
            print("暂无待办事项")
            return
        
        print("\n所有待办事项：")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")
    
    def list_pending(self):
        """显示未完成的事项"""
        pending = [item for item in self.items if not item.completed]
        if not pending:
            print("没有未完成的事项")
            return
        
        print("\n未完成的事项：")
        for item in pending:
            print(f"  {item}")
    
    def statistics(self):
        """统计信息"""
        total = len(self.items)
        completed = sum(1 for item in self.items if item.completed)
        pending = total - completed
        print(f"\n统计：总计{total}项，已完成{completed}项，待完成{pending}项")

# 测试待办事项管理器
todo_list = TodoList()
todo_list.add_item("学习Python基础", "变量、数据类型、控制流程", "高")
todo_list.add_item("完成项目文档", "", "中")
todo_list.add_item("锻炼身体", "跑步30分钟", "低")

todo_list.list_all()
todo_list.complete_item(0)
todo_list.list_all()
todo_list.statistics()


# ============================================
# 项目2：简单计算器
# ============================================

print("\n\n=== 项目2：简单计算器 ===\n")

class Calculator:
    """计算器类"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加法"""
        result = a + b
        self._save_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法"""
        result = a - b
        self._save_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乘法"""
        result = a * b
        self._save_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            return "错误：除数不能为0"
        result = a / b
        self._save_history(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """幂运算"""
        result = base ** exponent
        self._save_history(f"{base} ^ {exponent} = {result}")
        return result
    
    def _save_history(self, operation):
        """保存历史记录"""
        self.history.append(operation)
    
    def show_history(self):
        """显示历史记录"""
        if not self.history:
            print("暂无计算历史")
            return
        
        print("\n计算历史：")
        for i, record in enumerate(self.history, 1):
            print(f"{i}. {record}")
    
    def clear_history(self):
        """清空历史记录"""
        self.history.clear()
        print("历史记录已清空")

# 测试计算器
calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 × 5 = {calc.multiply(10, 5)}")
print(f"10 ÷ 5 = {calc.divide(10, 5)}")
print(f"2 ^ 8 = {calc.power(2, 8)}")

calc.show_history()


# ============================================
# 项目3：学生成绩管理系统
# ============================================

print("\n\n=== 项目3：学生成绩管理系统 ===\n")

class StudentGrade:
    """学生成绩类"""
    
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}
    
    def add_grade(self, subject, score):
        """添加成绩"""
        if 0 <= score <= 100:
            self.grades[subject] = score
            print(f"已添加 {self.name} 的{subject}成绩：{score}分")
        else:
            print("成绩必须在0-100之间")
    
    def get_average(self):
        """计算平均分"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_grade_level(self):
        """获取等级"""
        avg = self.get_average()
        if avg >= 90:
            return "优秀"
        elif avg >= 80:
            return "良好"
        elif avg >= 70:
            return "中等"
        elif avg >= 60:
            return "及格"
        else:
            return "不及格"
    
    def __str__(self):
        avg = self.get_average()
        level = self.get_grade_level()
        return f"{self.student_id} - {self.name}: 平均分{avg:.2f}分 ({level})"

class GradeManager:
    """成绩管理系统"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name):
        """添加学生"""
        if student_id not in self.students:
            self.students[student_id] = StudentGrade(student_id, name)
            print(f"已添加学生：{name} ({student_id})")
        else:
            print("学生ID已存在")
    
    def add_grade(self, student_id, subject, score):
        """添加成绩"""
        if student_id in self.students:
            self.students[student_id].add_grade(subject, score)
        else:
            print("学生不存在")
    
    def get_student_info(self, student_id):
        """查询学生信息"""
        if student_id in self.students:
            student = self.students[student_id]
            print(f"\n{student}")
            print(f"各科成绩：{student.grades}")
        else:
            print("学生不存在")
    
    def list_all_students(self):
        """列出所有学生"""
        if not self.students:
            print("暂无学生信息")
            return
        
        print("\n所有学生信息：")
        for student in sorted(self.students.values(), 
                            key=lambda s: s.get_average(), 
                            reverse=True):
            print(f"  {student}")
    
    def get_subject_statistics(self, subject):
        """科目统计"""
        scores = [s.grades.get(subject, 0) for s in self.students.values() 
                 if subject in s.grades]
        
        if not scores:
            print(f"{subject}暂无成绩")
            return
        
        avg = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        print(f"\n{subject}统计：")
        print(f"  平均分：{avg:.2f}")
        print(f"  最高分：{max_score}")
        print(f"  最低分：{min_score}")

# 测试成绩管理系统
manager = GradeManager()
manager.add_student("S001", "张三")
manager.add_student("S002", "李四")
manager.add_student("S003", "王五")

manager.add_grade("S001", "数学", 85)
manager.add_grade("S001", "英语", 90)
manager.add_grade("S001", "物理", 88)

manager.add_grade("S002", "数学", 92)
manager.add_grade("S002", "英语", 88)
manager.add_grade("S002", "物理", 95)

manager.add_grade("S003", "数学", 78)
manager.add_grade("S003", "英语", 82)
manager.add_grade("S003", "物理", 80)

manager.list_all_students()
manager.get_subject_statistics("数学")
manager.get_student_info("S001")


# ============================================
# 项目4：猜数字游戏
# ============================================

print("\n\n=== 项目4：猜数字游戏 ===\n")

class GuessingGame:
    """猜数字游戏"""
    
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = 10
    
    def guess(self, number):
        """猜数字"""
        self.attempts += 1
        
        if number < self.min_num or number > self.max_num:
            return f"请输入{self.min_num}到{self.max_num}之间的数字"
        
        if number == self.secret_number:
            return f"恭喜你！猜对了！答案是{self.secret_number}，你用了{self.attempts}次"
        elif number < self.secret_number:
            remaining = self.max_attempts - self.attempts
            return f"太小了！还有{remaining}次机会"
        else:
            remaining = self.max_attempts - self.attempts
            return f"太大了！还有{remaining}次机会"
    
    def is_game_over(self):
        """游戏是否结束"""
        return self.attempts >= self.max_attempts
    
    def get_hint(self):
        """获取提示"""
        mid = (self.min_num + self.max_num) // 2
        if self.secret_number <= mid:
            return f"提示：答案在{self.min_num}到{mid}之间"
        else:
            return f"提示：答案在{mid+1}到{self.max_num}之间"

# 测试猜数字游戏（自动演示）
game = GuessingGame(1, 100)
print(f"猜数字游戏：请猜一个{game.min_num}到{game.max_num}之间的数字")
print(f"提示：正确答案是 {game.secret_number}\n")

# 模拟猜测
test_guesses = [50, 75, 88, game.secret_number]
for guess_num in test_guesses:
    result = game.guess(guess_num)
    print(f"猜 {guess_num}: {result}")
    if guess_num == game.secret_number:
        break


# ============================================
# 项目5：简单的文本分析器
# ============================================

print("\n\n=== 项目5：文本分析器 ===\n")

class TextAnalyzer:
    """文本分析器"""
    
    def __init__(self, text):
        self.text = text
        self.words = text.split()
    
    def word_count(self):
        """统计词数"""
        return len(self.words)
    
    def character_count(self, include_spaces=True):
        """统计字符数"""
        if include_spaces:
            return len(self.text)
        else:
            return len(self.text.replace(" ", ""))
    
    def sentence_count(self):
        """统计句子数"""
        separators = ['.', '!', '?', '。', '！', '？']
        count = sum(self.text.count(sep) for sep in separators)
        return max(count, 1)
    
    def word_frequency(self):
        """词频统计"""
        freq = {}
        for word in self.words:
            word = word.lower().strip('.,!?;:')
            freq[word] = freq.get(word, 0) + 1
        return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    
    def most_common_words(self, n=5):
        """最常见的n个词"""
        freq = self.word_frequency()
        return list(freq.items())[:n]
    
    def analyze(self):
        """综合分析"""
        print(f"文本分析报告：")
        print(f"  字符数（含空格）：{self.character_count(True)}")
        print(f"  字符数（不含空格）：{self.character_count(False)}")
        print(f"  词数：{self.word_count()}")
        print(f"  句子数：{self.sentence_count()}")
        print(f"\n最常见的5个词：")
        for word, count in self.most_common_words(5):
            print(f"    '{word}': {count}次")

# 测试文本分析器
sample_text = """
Python is a high-level programming language. Python is easy to learn and Python is powerful.
Many developers love Python because Python has excellent libraries and Python community support.
"""

analyzer = TextAnalyzer(sample_text)
analyzer.analyze()


print("\n\n" + "="*50)
print("🎉 恭喜你完成Python速成教程！")
print("="*50)
print("""
你已经学习了：
✓ 第1课：基础语法（变量、数据类型、运算符）
✓ 第2课：控制流程（if-else、循环、异常处理）
✓ 第3课：函数和模块（函数定义、参数、Lambda）
✓ 第4课：数据结构（列表、元组、字典、集合）
✓ 第5课：面向对象编程（类、继承、封装、多态）
✓ 第6课：实战项目（综合应用）

下一步建议：
1. 学习Python标准库（os, sys, datetime, json等）
2. 学习文件操作和数据库
3. 学习Web开发（Flask/Django）或数据分析（pandas/numpy）
4. 多做项目实践，巩固所学知识
5. 阅读优秀的开源代码，学习最佳实践

继续加油！💪
""")
