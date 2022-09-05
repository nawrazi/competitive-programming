# https://codeforces.com/gym/397282/problem/C

from collections import defaultdict

l = int(input())
s = input()

rel = {'0': -1, '1': 1}
tot = [0]

for i in range(l):
    tot.append(tot[i] + rel[s[i]])

firlas = defaultdict(lambda: [None, None])

for i, n in enumerate(tot):
    if firlas[n][0] is None:
        firlas[n][0] = i
    firlas[n][1] = i

maxim = 0
for fl in firlas.values():
    maxim = max(maxim, fl[1] - fl[0])

print(maxim)
