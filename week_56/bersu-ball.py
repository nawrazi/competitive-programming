# https://codeforces.com/gym/425420/problem/B

n = int(input())
boys = sorted(int(n) for n in input().split())
m = int(input())
girls = sorted(int(n) for n in input().split())

b, g = 0, 0
pairs = 0

while b < n and g < m:
    if boys[b] + 1 < girls[g]:
        b += 1
    elif girls[g] + 1 < boys[b]:
        g += 1
    else:
        pairs += 1
        b += 1
        g += 1
        
print(pairs)
