"""
Python速成教程 - 第5课：面向对象编程
学习内容：类、对象、继承、多态、封装
"""

# ============================================
# 1. 类和对象基础
# ============================================

print("=== 1. 类和对象基础 ===")

# 定义一个简单的类
class Dog:
    """狗类"""
    
    def __init__(self, name, age):
        """构造函数"""
        self.name = name
        self.age = age
    
    def bark(self):
        """狗叫"""
        print(f"{self.name}说：汪汪汪！")
    
    def get_info(self):
        """获取信息"""
        return f"{self.name}，{self.age}岁"

# 创建对象
dog1 = Dog("旺财", 3)
dog2 = Dog("小黑", 2)

# 调用方法
print(dog1.get_info())
dog1.bark()

print(dog2.get_info())
dog2.bark()


# ============================================
# 2. 类属性和实例属性
# ============================================

print("\n=== 2. 类属性和实例属性 ===")

class Circle:
    """圆形类"""
    
    # 类属性（所有实例共享）
    pi = 3.14159
    count = 0
    
    def __init__(self, radius):
        """构造函数"""
        # 实例属性（每个实例独有）
        self.radius = radius
        Circle.count += 1
    
    def area(self):
        """计算面积"""
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        """计算周长"""
        return 2 * Circle.pi * self.radius

# 创建圆形对象
c1 = Circle(5)
c2 = Circle(3)

print(f"圆1：半径={c1.radius}, 面积={c1.area():.2f}, 周长={c1.circumference():.2f}")
print(f"圆2：半径={c2.radius}, 面积={c2.area():.2f}, 周长={c2.circumference():.2f}")
print(f"总共创建了 {Circle.count} 个圆")


# ============================================
# 3. 继承
# ============================================

print("\n=== 3. 继承 ===")

# 父类（基类）
class Animal:
    """动物类"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """发声"""
        print(f"{self.name}发出声音")
    
    def move(self):
        """移动"""
        print(f"{self.name}在移动")

# 子类1
class Cat(Animal):
    """猫类，继承自动物类"""
    
    def speak(self):
        """重写父类方法"""
        print(f"{self.name}说：喵喵喵~")
    
    def climb(self):
        """猫特有的方法"""
        print(f"{self.name}在爬树")

# 子类2
class Bird(Animal):
    """鸟类，继承自动物类"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # 调用父类构造函数
        self.can_fly = can_fly
    
    def speak(self):
        """重写父类方法"""
        print(f"{self.name}说：叽叽喳喳~")
    
    def fly(self):
        """鸟特有的方法"""
        if self.can_fly:
            print(f"{self.name}在飞翔")
        else:
            print(f"{self.name}不会飞")

# 使用子类
cat = Cat("小花")
cat.speak()
cat.move()
cat.climb()

print()

bird = Bird("小鸟")
bird.speak()
bird.move()
bird.fly()

penguin = Bird("企鹅", can_fly=False)
penguin.fly()


# ============================================
# 4. 封装（私有属性和方法）
# ============================================

print("\n=== 4. 封装 ===")

class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 私有属性（双下划线开头）
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存款 {amount} 元，当前余额：{self.__balance} 元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"取款 {amount} 元，当前余额：{self.__balance} 元")
            else:
                print("余额不足")
        else:
            print("取款金额必须大于0")
    
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    def __secret_operation(self):
        """私有方法"""
        print("这是私有方法，外部无法调用")

# 使用银行账户
account = BankAccount("张三", 1000)
account.deposit(500)
account.withdraw(300)
print(f"账户余额：{account.get_balance()} 元")

# 无法直接访问私有属性
# print(account.__balance)  # 这会报错


# ============================================
# 5. 多态
# ============================================

print("\n=== 5. 多态 ===")

class Shape:
    """形状基类"""
    
    def area(self):
        """计算面积"""
        pass
    
    def describe(self):
        """描述"""
        print(f"这是一个形状，面积为 {self.area():.2f}")

class Rectangle(Shape):
    """矩形"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    """三角形"""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class CircleShape(Shape):
    """圆形"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# 多态：不同对象调用相同方法，表现出不同行为
shapes = [
    Rectangle(5, 4),
    Triangle(6, 3),
    CircleShape(3)
]

print("各种形状：")
for shape in shapes:
    shape.describe()


# ============================================
# 6. 特殊方法（魔术方法）
# ============================================

print("\n=== 6. 特殊方法 ===")

class Point:
    """点类"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示（用于print）"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """官方字符串表示"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """加法运算符重载"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """相等运算符重载"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """长度（到原点的距离）"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# 使用特殊方法
p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"p1: {p1}")  # 调用 __str__
print(f"p2: {p2}")
print(f"p1 + p2 = {p1 + p2}")  # 调用 __add__
print(f"p1 == p2: {p1 == p2}")  # 调用 __eq__
print(f"p1到原点距离: {len(p1)}")  # 调用 __len__


# ============================================
# 7. 类方法和静态方法
# ============================================

print("\n=== 7. 类方法和静态方法 ===")

class MathUtils:
    """数学工具类"""
    
    pi = 3.14159
    
    @classmethod
    def circle_area(cls, radius):
        """类方法：计算圆面积"""
        return cls.pi * radius ** 2
    
    @staticmethod
    def is_even(n):
        """静态方法：判断是否为偶数"""
        return n % 2 == 0
    
    @staticmethod
    def factorial(n):
        """静态方法：计算阶乘"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# 不需要创建实例就可以调用
print(f"半径为5的圆面积：{MathUtils.circle_area(5):.2f}")
print(f"10是偶数：{MathUtils.is_even(10)}")
print(f"5的阶乘：{MathUtils.factorial(5)}")


# ============================================
# 练习题
# ============================================

print("\n=== 练习题 ===")

# 练习1：创建一个学生类
class Student:
    """学生类"""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}
    
    def add_course(self, course_name, score):
        """添加课程成绩"""
        self.courses[course_name] = score
    
    def get_average(self):
        """计算平均分"""
        if not self.courses:
            return 0
        return sum(self.courses.values()) / len(self.courses)
    
    def __str__(self):
        avg = self.get_average()
        return f"学生：{self.name}（{self.student_id}），平均分：{avg:.2f}"

# 测试学生类
student = Student("李明", "2024001")
student.add_course("数学", 85)
student.add_course("英语", 90)
student.add_course("物理", 88)
print(f"\n{student}")
print(f"课程成绩：{student.courses}")


# 练习2：创建一个书籍管理系统
class Book:
    """书籍类"""
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"《{self.title}》 - {self.author} ({status})"

class Library:
    """图书馆类"""
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """添加书籍"""
        self.books.append(book)
        print(f"添加书籍：{book.title}")
    
    def borrow_book(self, isbn):
        """借书"""
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"成功借阅：{book.title}")
                    return True
                else:
                    print(f"{book.title} 已被借出")
                    return False
        print("未找到该书籍")
        return False
    
    def return_book(self, isbn):
        """还书"""
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"成功归还：{book.title}")
                    return True
                else:
                    print(f"{book.title} 未被借出")
                    return False
        print("未找到该书籍")
        return False
    
    def list_books(self):
        """列出所有书籍"""
        print("\n图书馆藏书：")
        for book in self.books:
            print(f"  {book}")

# 测试图书管理系统
library = Library()
library.add_book(Book("Python编程", "张三", "001"))
library.add_book(Book("数据结构", "李四", "002"))
library.add_book(Book("算法导论", "王五", "003"))

library.list_books()

print("\n借阅操作：")
library.borrow_book("001")
library.borrow_book("001")  # 已借出

print("\n归还操作：")
library.return_book("001")

library.list_books()

print("\n✅ 第5课完成！面向对象是高级编程的基础！")
