# https://codeforces.com/gym/397282/problem/E

from heapq import heappop, heappush

def solve():
    t = int(input())
    for _ in range(t):
        _ = input()
        l, a = [int(i) for i in input().split()]
        acs = [int(i) for i in input().split()]
        temps = [int(i) for i in input().split()]

        land = [None for _ in range(l)]
        h = []
        for i in range(a):
            heappush(h, (temps[i], acs[i] - 1))

        while h:
            temp, pos = heappop(h)
            if land[pos] is not None:
                continue

            land[pos] = temp

            for nex in [pos + 1, pos - 1]:
                if nex < 0 or nex >= l:
                    continue
                heappush(h, (temp + 1, nex))

        print(*land)

solve()
