# https://codeforces.com/gym/421762/problem/C

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort(reverse=True)
    grps = []
    last = None
    
    for a in arr:
        if a != last:
            grps.append(1)
            last = a
        else:
            grps[-1] += 1
            
    prefix = 0
    total = sum(grps)
    most = 0
    
    for i in range(len(grps)):
        prefix += grps[i]
        cur = prefix * (total - prefix)
        lvl = grps[i] // 2
        most = max(most, cur, lvl)
        
    print(most)
    
