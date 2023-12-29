from random import randint
import os

with open('sow.txt','w',encoding='utf-8') as f:
    for i in range(100):
        f.write(f"192.168.1.{randint(0,50)}\n")


