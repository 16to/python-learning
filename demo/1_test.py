# 圆周面积和周长
import math

radius = 5
area =  math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"半径为 {radius} 的圆：")
print(f"面积 = {area:.2f}")
print(f"周长 = {circumference:.2f}")

# 字符串操作
str = "Hello World"
# 首字母小写
str_lower = str.lower()
print(str_lower)
# 判断是否是什么开头
print(str.startswith("Hello"))
print(str.startswith("hello"))