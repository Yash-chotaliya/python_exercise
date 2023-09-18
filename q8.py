n = int(input())
n1 = n
n2 = 0

while n>0:
    n2 = (n2*10) + (n%10)
    n = int(n/10)

if n1==n2:
    print(True)
else:
    print(False)