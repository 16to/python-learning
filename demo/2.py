# 条件语句
age = 18
if age >= 18:
    print(f"成年{age}")

if age >= 60:
    print(f"老人{age}")
else:
    print(f"小人{age}")

score = 90
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 比较运算符和逻辑运算符
a = 100
b = 99
if a == b:
    print("a == b")
if a != b:
    print("a != b")

is_man = True
is_allow = False

print(is_allow and is_man)
print(is_allow or is_man)
print(not is_allow)

# 循环
fruits = ["banner", "apple", "origer"]

for index, item in enumerate(fruits):
    print(index)
    print(item)

## 头包尾不包
for i in range(1,101):
    print(f"i={i}")
    if i % 2 == 0:
        print(i)
## while循环
count = 1
while count <= 5:
    if count % 2 == 0:
        count += 1
        continue
    if count == 5:
        print("last number")
        break
    count += 1
print(f"循环结束{count}")

# 列表推导

lists = []
for i in range(0,6):
    lists.append(i ** 2)
print(lists)

# 异常处理
try:
    number = int("abc")
except ValueError:
    print(ValueError)
finally:
    print("exec")