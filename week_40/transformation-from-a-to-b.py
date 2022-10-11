# https://codeforces.com/gym/403303/problem/B

from collections import defaultdict, deque

a, b = [int(n) for n in input().split()]
q = deque([(a)])
path = defaultdict(int)
path[a] = None
ans = []

while q:
    num = q.popleft()

    if num == b:
        cur = num
        while cur:
            ans.append(cur)
            cur = path[cur]
        break

    if num * 2 not in path and num * 2 <= b:
        path[num * 2] = num
        q.append(num * 2)
    if (num * 10) + 1 not in path and (num * 10) + 1 <= b:
        path[(num * 10) + 1] = num
        q.append((num * 10) + 1)

if ans:
    ans.reverse()
    print('YES')
    print(len(ans))
    print(*ans)
else:
    print('NO')
    
