# https://codeforces.com/problemset/problem/1351/B

for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    c, d = [int(i) for i in input().split()]
    
    if a == c and b + d == a:
        print('Yes')
        
    elif a == d and b + c == a:
        print('Yes')
        
    elif b == c and a + d == b:
        print('Yes')
        
    elif b == d and a + c == b:
        print('Yes')
        
    else:
        print('No')
        
