# https://codeforces.com/gym/407211/problem/A

for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 1:
            print('NO')
            break
    else:
        print('YES')
        
