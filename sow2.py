import os

with open('sow.txt','r',encoding='utf-8') as f:
    count = 0
    while True:
        line = f.readline()
        if line == "192.168.1.6\n":
            count += 1
        if line == "":
            break
    print(count)

with open('sow.txt', 'r', encoding='utf-8') as f:
    counts = 0
    for line in f:
        if line == "192.168.1.1\n":
            counts += 1
    print(counts)
