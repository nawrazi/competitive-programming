# https://codeforces.com/contest/1779/problem/B

for _ in range(int(input())):
    n = int(input())
    arr = []
    
    if n == 3:
        print('NO')
        continue
        
    if n % 2 == 0:
        val = 1
        for _ in range(n):
            arr.append(val)
            val *= -1
            
    else:
        val = n // 2
        for _ in range(n // 2):
            arr.append(val - 1)
            arr.append(-val)
        arr.append(val - 1)
        
    print('YES')
    print(*arr)
    
