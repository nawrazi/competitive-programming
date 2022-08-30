# https://codeforces.com/contest/1714/problem/C

t = int(input())
for _ in range(t):
    num = int(input())
    ans = []
    for i in range(9, 0, -1):
        if num >= i:
            ans.append(i)
            num -= i
        
    print(''.join([str(n) for n in reversed(ans)]))
    
