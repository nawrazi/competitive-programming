t = int(input())
for _ in range(t):
    earliest, latest = {}, {}
    b = input()
    nq = input()
    n, q = nq.split()
    stops = input().split()
    for i, stop in enumerate(stops):
        if stop not in earliest:
            earliest[stop] = i
        latest[stop] = i
    for _ in range(int(q)):
        s, e = input().split()
        if s not in latest or e not in latest:
            print('NO')
        else:
            if earliest[s] <= latest[e]:
                print('YES')
            else:
                print('NO')
