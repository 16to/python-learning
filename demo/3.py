# 函数
def hello(name) -> bool:
    print(f"hello {name}")
    return True


hello("world")


# 函数参数
def sum(a, b) -> int:
    return a + b


print(sum(b=3, a=2))  # 关键词参数，可以不讲顺序


def sum_all(first_number, *number) -> int:
    print(first_number, number, type(number))
    total = 0
    total += first_number
    for num in number:
        total += num
    return total


print(sum_all(99, 2, 3, 4, 5, 6))

# Lambda表达式
students = [
    {"name": "A", "score": 99},
    {"name": "B", "score": 70},
    {"name": "C", "score": 80},
]

sorted_students = sorted(students, key = lambda s: s["score"], reverse=True)

print(sorted_students)

# 变量作用域
g_val = 1

def scope():
    print(g_val)
    g_val += 1
    l_val = 2

print(g_val)
# print(l_val) # 报错

# 内置函数
