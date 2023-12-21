dict1 = {}
dict2 = dict()
dict3 = {'name': 'earth', 'port': 80}


print(type(dict1))
print(type(dict2))
print(type(dict3))

dict1['name'] = 'earth'

print(dict1)
dict1['name'] = "marks"

print(dict1)

print(dict1.get('name'))
print(dict1["name"])

del dict1['name']

print(dict1)