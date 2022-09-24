# https://codeforces.com/problemset/problem/1734/B

t = int(input())
for _ in range(t):
    n = int(input())
    print(1)
    for i in range(2, n + 1):
        floor = [1] + [0 for _ in range(i - 2)] + [1]
        print(*floor)
        
