# https://codeforces.com/gym/395482/problem/A

def solve():
    levels = int(input())
    p = [int(i) for i in input().split()]
    q = [int(i) for i in input().split()]
    p.pop(0)
    q.pop(0)
    total = set(p) | set(q)
    for i in range(1, levels + 1):
        if i not in total:
            print('Oh, my keyboard!')
            return
    print('I become the guy.')

solve()
