l1 = [10,20,30,40,50]
l2 = [5,10,15,20,25]
l = []

for i in range(len(l1)):
    if(i%2!=0):
        l.append(l1[i])
        
for i in range(len(l2)):
    if(i%2==0):
        l.append(l2[i])
        
print(l)