# https://codeforces.com/gym/421762/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    stack = [float('inf')]
    found = False
    for a in arr:
        if stack and found and a < stack[-1]:
            print('NO')
            break
            
        while stack and a <= stack[-1]:
            stack.pop()
            
        if stack and a > stack[-1]:
            found = True
            
        stack.append(a)
        
    else:
        print('YES')
        
