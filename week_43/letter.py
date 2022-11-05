# https://codeforces.com/gym/408379/problem/B

string = input()

caps = []
smalls = []
c, s = 0, 0
for cr in string:
    smalls.append(c)
    if cr.islower():
        c += 1

for cr in reversed(string):
    caps.append(s)
    if cr.isupper():
        s += 1
caps.reverse()

ans = float('inf')
for i in range(len(string)):
    cur = smalls[i] + caps[i]
    ans = min(ans, cur)

print(ans)
