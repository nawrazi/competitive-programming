# https://codeforces.com/gym/397282/problem/B

def solve():
    t = int(input())
    for _ in range(t):
        m, n = [int(i) for i in input().split()]
        mat = []
        for _ in range(m):
            mat.append(list(input()))

        for c in range(n):
            stones = 0
            for r in range(m):
                if mat[r][c] == '*':
                    mat[r][c] = '.'
                    stones += 1
                if mat[r][c] == 'o' or r == m - 1:
                    cur = r
                    if mat[r][c] == 'o':
                        cur -= 1
                    while stones:
                        mat[cur][c] = '*'
                        stones -= 1
                        cur -= 1

        for row in mat:
            print(''.join(row))
        print()

solve()
