import random

from openpyxl import workbook
wb = workbook.Workbook()
sh = wb.active
for i in range(1,101):
    sh[f"A{i}"] = random.randint(1,101)
wb.save("test5.xlsx")

