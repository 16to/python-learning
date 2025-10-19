# 圆周面积和周长
import math

radius = float(input("请输入圆的半径: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"圆的面积: {area}")
print(f"圆的周长: {circumference}")