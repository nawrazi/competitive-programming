# https://codeforces.com/gym/404077/problem/A

from collections import defaultdict

n = int(input())
s = input()
count = len(set(s))

best = float('inf')
cur = defaultdict(int)
i, j = 0, 0
while j < n:
    cur[s[j]] += 1
    if len(cur) == count:
        while i <= j and len(cur) == count:
            best = min(best, j - i + 1)
            cur[s[i]] -= 1
            if cur[s[i]] == 0:
                del cur[s[i]]        
            i += 1
    j += 1

print(best)
