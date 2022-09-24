# https://codeforces.com/gym/400361/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(n) for n in input().split()]
    seen = set()
    f = 0
    for i, num in enumerate(reversed(nums)):
        if num not in seen:
            seen.add(num)
        else:
            f = n - i
            break

    print(f)
    
