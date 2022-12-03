# https://codeforces.com/gym/413954/problem/B

input()
arr = [int(i) for i in input().split()]

count = {0: float('inf'), 4: 0, 8: 0, 15: 0, 16: 0, 23: 0, 42: 0}
prev = {4: 0, 8: 4, 15: 8, 16: 15, 23: 16, 42: 23}

rem = 0
for a in arr:
    if count[a] >= count[prev[a]]:
        rem += 1
    else:
        count[a] += 1
        
count.pop(0)
if count[4] != count[42]:
    prev = count[4]
    for i, c in enumerate(count.values()):
        if c != prev:
            rem += i * (prev - c)
        prev = c
        
print(rem)
