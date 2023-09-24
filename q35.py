keys = ['a', 'b', 'c']
values = [1, 2, 3]

dict = {}

for i in range(len(keys)):
    dict.update({keys[i]:values[i]})
print(dict)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)
