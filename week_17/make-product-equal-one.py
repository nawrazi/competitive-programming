def solve(nums):
    coins = 0
    negs = 0
    any_zeros = False
    for num in nums:
        if num < 0:
            coins += (-1 - num)
            negs += 1
        elif num > 0:
            coins += (num - 1)
        else:
            any_zeros = True
            coins += 1

    if negs % 2 != 0 and not any_zeros:
        coins += 2

    print(coins)


n = int(input())
nums = [int(i) for i in input().split()]
solve(nums)
