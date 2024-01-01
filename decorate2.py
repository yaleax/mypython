from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('test5.xlsx')
ws = wb.active
index = []
tem = []
for i,cell in enumerate(ws['A']):
    print(i,cell.value)
    flag = cell.value not in tem
    if flag:
        tem.append(cell.value)
    else:
        index.append(i)

print(index)
print(tem)