# https://codeforces.com/contest/1743/problem/A

def combination(n, r):
    cache = {1: 1, 0: 1}
    def factorial(n):
        if n not in cache:
            cache[n] = n * factorial(n - 1)

        return cache[n]
    
    return factorial(n) // (factorial(n - r) * factorial(r))

for _ in range(int(input())):
    input()
    n = (len(input()) // 2) + 1
    print(combination(10 - n, 2) * 6)
    
