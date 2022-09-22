# https://codeforces.com/problemset/problem/1704/C

t = int(input())
for _ in range(t):
    total, all_inf = [int(n) for n in input().split()]
    inf = sorted(int(n) for n in input().split())
    gaps = [(inf[0] - 1) + (total - inf[-1])]
    for i in range(all_inf - 1):
        gaps.append(inf[i + 1] - inf[i] - 1)

    round = 0
    protected = 0
    for gap in reversed(sorted(gaps)):
        prot = gap - round - 1
        if prot == 0:
            protected += 1
        if prot <= 0:
            break
        protected += prot
        round += 4

    print(total - protected)
    
