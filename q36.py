dict = {
    1:"one",
    2:"two",
    3:"three",
    7:"seven",
    9:"nine"
}

set = [3,7]

for i in range(len(set)):
    
    dict.pop(set[i])
    
print(dict)