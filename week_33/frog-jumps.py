# https://codeforces.com/problemset/problem/1324/C

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        s += 'R'
        cur = 0
        max_con = 0
        for c in s:
            if c == 'R':
                max_con = max(max_con, cur)
                cur = 0
            else:
                cur += 1

        print(max_con + 1)

solve()
