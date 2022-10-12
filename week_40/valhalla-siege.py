# https://codeforces.com/gym/403606/problem/C

def bisect(off, target):
    start, end = 0, n - 1
    best = n
    while start <= end:
        mid = (start + end) // 2
        if target > war[mid] - off:
            start = mid + 1
        elif target < war[mid] - off:
            best = mid
            end = mid - 1
        else:
            best = mid + 1
            start = mid + 1

    return best

n, q = [int(i) for i in input().split()]
war = [int(i) for i in input().split()]
att = [int(i) for i in input().split()]

cur = 0
for i in range(n):
    cur += war[i]
    war[i] = cur

off = 0
for a in att:
    i = bisect(off, a)
    print(n - i if i < n else n)

    off += a
    if off >= war[-1]:
        off = 0
        
