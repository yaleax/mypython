# 要求 用户输入数字，然后求平均值 按Q退出
# 1.输入数字
# 2.求和
# 3.求平均值
# 4.按Q退出
# 5.循环
while True:
    total = 0
    count = 0
    user_input = input("请输入数字我会帮你求和，按Q退出：")
    while user_input != "Q" and user_input != "q":
        total += float(user_input)
        count += 1
        user_input = input("请输入数字我会帮你求和，按Q退出：")
    if count == 0:
        result = 0
    else:
        result = total / count
        print("平均值是：" + str(result))

    repeat = input("是否退出？按y/n：")
    if repeat == "Y" or repeat == "y":
        break
print("程序结束")