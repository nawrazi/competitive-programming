# https://codeforces.com/gym/403303/problem/C

from collections import defaultdict

n, m = [int(n) for n in input().split()]
dep = defaultdict(int)

for _ in range(m):
    a, b = [int(n) for n in input().split()]
    dep[a] += 1
    dep[b] += 1

ones, twos, most = 0, 0, 0
for i, d in dep.items():
    if d == 1:
        ones += 1
    if d == 2:
        twos += 1
    most = max(most, d)

path = set()
if ones == 2 and twos == n - 2:
    print('bus topology')
elif twos == n:
    print('ring topology')
elif ones == n - 1 and most == n - 1:
    print('star topology')
else:
    print('unknown topology')
    
