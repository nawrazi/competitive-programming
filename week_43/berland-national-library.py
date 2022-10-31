# https://codeforces.com/gym/407211/problem/B

vis = set()
size = 0
for _ in range(int(input())):
    sign, idn = input().split()
    if sign == '+':
        vis.add(idn)
        size = max(size, len(vis))
    elif idn in vis:
        vis.remove(idn)
        size = max(size, len(vis))
    else:
        size = max(size, size + 1)
        
print(size)
