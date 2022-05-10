# https://codeforces.com/contest/1676/problem/A

def solve(ticket):
    if sum(ticket[:3]) == sum(ticket[3:]):
        print('YES')
    else:
        print('NO')

t = int(input())
for _ in range(t):
    ticket = [int(n) for n in list(input())]
    solve(ticket)
