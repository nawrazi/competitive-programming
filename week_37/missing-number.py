# https://cses.fi/problemset/task/1083

n = int(input())
nums = {int(n) for n in input().split()}
for i in range(1, n + 1):
    if i not in nums:
        print(i)