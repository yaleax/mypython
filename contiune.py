from random import randint

for i in range(10):
    num = randint(3, 10)
    print(f"========第{i+1}部评分是：{num}分")
    print("点赞")
    if num < 8:
        continue
    print("收藏")
    print("转发")


