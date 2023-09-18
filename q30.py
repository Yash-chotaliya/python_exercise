l = [1,2,5,3,6,4,5]

dict = {}

for i in range(len(l)):
    dict[l[i]] = l.count(l[i])

print(dict)