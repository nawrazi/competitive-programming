# https://codeforces.com/gym/408379/problem/C

from collections import defaultdict

for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    needs = defaultdict(int)
    for a in arr:
        diff = k - (a % k)
        if a % k != 0:
            needs[diff] += 1
            
    sor = [(need, mod) for mod, need in needs.items()]
    sor.sort()
    if not sor:
        print(0)
        continue
        
    need, mod = sor[-1]
    print(mod + (k * (need - 1)) + 1)
    
