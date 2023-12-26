print("去逛街啦！")

i = 0
while i < 3:
    response = input("这家好吗？(y/n): ")
    if response == "n":
        print("下一家")
    elif response == "y":
        print("买买买")
        break
    i += 1

print("不逛街啦！")

