# https://codeforces.com/contest/1744/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(n) for n in input().split()]
    s = input()
    nl = {}
    for i in range(n):
        if nums[i] not in nl:
            nl[nums[i]] = s[i]

        elif nl[nums[i]] != s[i]:
                print('NO')
                break
    else:
        print('YES')
        
