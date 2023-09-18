count=1;

with open('samp1.txt',"a") as file1, open('samp.txt',"r") as file:
    for line in file:
        if(count!=5):
            file1.write(line)
        count=count+1