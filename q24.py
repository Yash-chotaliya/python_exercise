def recure(n):
    if n==0:
        return 0
    else:
        return n+recure(n-1)
    
result = recure(10)
print(result)