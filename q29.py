l1 = [1,2,3,4,5,6,7,8,9]
l2 = [11,12,13,14,15,16,17,18]

l3 = []

for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i])
        
for i in range(len(l2)):
    if i%2==0:
        l3.append(l2[i])
        
print(l3)