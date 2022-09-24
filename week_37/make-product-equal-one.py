# https://codeforces.com/gym/400361/problem/C

n = int(input())
nums = [int(n) for n in input().split()]
negs = 0
zeros = False
coins = 0 
for num in nums:
    if num == 0:
        zeros = True
    if num < 0:
        negs += 1
    coins += abs(abs(num) - 1)

if negs % 2 == 1 and not zeros:
    coins += 2

print(coins)
