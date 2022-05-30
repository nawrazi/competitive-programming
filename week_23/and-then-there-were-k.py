t = int(input())
for _ in range(t):
    n = int(input())
    while n != 0:
        k = n-1
        n &= k
 
    print(k)