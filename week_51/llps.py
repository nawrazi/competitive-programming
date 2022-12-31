# https://codeforces.com/gym/419374/problem/A

from collections import Counter

s = input()
m = 0
for c in s:
    m = max(ord(c), m)
    
print(chr(m) * Counter(s)[chr(m)])
