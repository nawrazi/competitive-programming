# https://codeforces.com/gym/371751/problem/A

from collections import deque

def find(target):
    q = deque([(31,31), (32,32)])

    while q:
        num, source = q.popleft()
        if num == target:
            return source
        if num > target:
            q.append((num-1, source))
        if num < target:
            q.append((num+4, source))

    return -1


t = int(input())
for _ in range(t):
    target = int(input())
    print(find(target))
