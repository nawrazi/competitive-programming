# https://codeforces.com/gym/394494/problem/C

t = int(input())
for _ in range(t):
    n, target = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    counts = { 2 ** i: 0 for i in range(31) }

    final = 0
    for i in range(30, -1, -1):
        mask = 2 ** i
        count = 0
        for num in nums:
            if num & mask == 0:
                count += 1
        
        if count <= target:
            target -= count
            final += mask
        
    print(final)
