# https://codeforces.com/gym/393453/problem/A

t = int(input())
for _ in range(t):
    b = [int(i) for i in input().split()]
    a = []
    a.append(b[0])
    a.append(b[1])
    if b[2] == sum(a):
        a.append(b[3])
    else:
        a.append(b[2])
    print(*a)