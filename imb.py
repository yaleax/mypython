
you_weight = input("请输入你的体重KG:")
you_hight = input("请输入你的身高CM:")

BMI = (float(you_weight) / (float(you_hight) * float(you_hight))) * 10000
BMI = round(BMI,2)
print("你的BMI指数为：",BMI)
if BMI < 18.5:
    print("你的体重过轻")
elif BMI >= 18.5 and BMI < 25:
    print("你的体重正常")
elif BMI >= 25 and BMI < 28:
    print("你的体重过重")
elif BMI >= 28 and BMI < 32:
    print("你的体重肥胖")
else:
    print("你的体重严重肥胖")

