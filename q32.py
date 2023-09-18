l = [5,3,4,6,1]
not_exist=[]

dict = {5:"5",
        3:"3",
        2:"2",
        6:"6"
        }

dictk = dict.keys()

for i in range(len(l)):
    if(dict.get(l[i])==None):
        not_exist.append(l[i])
    
for i in range(len(not_exist)):    
    l.remove(not_exist[i])

print(l)