# https://codeforces.com/gym/394494/problem/B

t = int(input())
for _ in range(t):
    n = input()
    bracks = input()
    open = 0
    for b in bracks:
        if b == '(':
            open += 1
        elif open > 0:
            open -= 1

    print(open)