# https://codeforces.com/gym/411140/problem/A

for _ in range(int(input())):
    input()
    red = [int(i) for i in input().split()]
    input()
    blue = [int(i) for i in input().split()]
    
    max_r = 0
    pre_r = 0
    for r in red:
        pre_r += r
        max_r = max(max_r, pre_r)
        
    max_b = 0
    pre_b = 0
    for b in blue:
        pre_b += b
        max_b = max(max_b, pre_b)
        
    print(max_r + max_b)
    
