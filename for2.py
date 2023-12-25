total = 0

for i in range(1,101):
    total += i
print(total)

list = [["hello","world"],["nihao","shijie"]]

for count,list1 in enumerate(list):
    for i in list1:
        print(count+1)
        print(i)
