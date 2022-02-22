(n,l,r) = [int(n) for n in input().split()]
ones = 0

def operation(n,l,r):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        base = [1,0,1]
        return sum(base[l-1:r])
    if n==3:
        base = [1,1,1]
        return sum(base[l-1:r])

    if n%2==0:
        return operation(n//2,l,None) + operation(n//2,0,r-((n//2)+1))
    else:
        return operation(n//2,l,n//2) + operation(n//2,0,r-((n//2)+1)) + 1

print(operation(n,l,r))
