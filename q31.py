l1 = ['a','b','c']
l2 = [0,1,2]

set = set()

for i in range(len(l2)):
    set.add(str(l1[i])+str(l2[i]))
    
print(set)