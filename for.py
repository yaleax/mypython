total = 0

for i in range(1, 101):
    total += i

print(total)


temperature = {"111": 33.5, "222": 34.5, "333": 35.5, "444": 36.5, "555": 37.5, "666": 38.5, "777": 39.5, "888": 40.5,}

for key, value in temperature.items():
    if value > 37.2:
        print(key + "工号的员工体温超过了37.2：" + str(value))
for key, value in temperature.items():
    print(key, value)