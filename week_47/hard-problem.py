# https://codeforces.com/gym/412541/problem/A

n = int(input())
cost = [int(i) for i in input().split()]
normal = []
reverse = []
for _ in range(n):
    s = input()
    normal.append(s)
    reverse.append(s[::-1])
    
ndp = [float('inf') for _ in range(n - 1)] + [0]
rdp = [float('inf') for _ in range(n - 1)] + [cost[-1]]

for i in range(n - 2, -1, -1):
    if normal[i] <= normal[i+1]:
        ndp[i] = min(ndp[i], ndp[i+1])
        
    if normal[i] <= reverse[i+1]:
        ndp[i] = min(ndp[i], rdp[i+1])
        
    if reverse[i] <= normal[i+1]:
        rdp[i] = min(rdp[i], cost[i] + ndp[i+1])
        
    if reverse[i] <= reverse[i+1]:
        rdp[i] = min(rdp[i], cost[i] + rdp[i+1])
        
if ndp[0] == rdp[0] == float('inf'):
    print(-1)
else:
    print(min(ndp[0], rdp[0]))
    
