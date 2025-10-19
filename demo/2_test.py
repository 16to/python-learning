# 9*9 乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

# 斐波那契数列
fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[i - 2] + fib[i - 1])
print(fib)
print(len(fib))

# 猜数字
import random

min = 0
max = 100
rand = random.randint(min, 100)

while True:
    try:
        guess = int(input(f"请输入{min}到{max}的数字："))
        if guess > max:
            print("范围错误")
            continue
        if guess < min:
            print("范围错误")
            continue
    except:
        print("格式错误")
        continue
    if guess == rand:
        print(f"恭喜猜中{guess}，游戏结束")
        break
    elif guess < rand:
        min = guess
        print(f"数字太小了")
    else:
        max = guess
        print(f"数字太大了")
