# https://codeforces.com/gym/395482/problem/C

def solve():
    t = int(input())
    for _ in range(t):
        _, total = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        s, e = 0, 0
        cur_total = 0
        best_len = -1
        best_range = [-float('inf'), -float('inf')]
        for i in range(len(nums)):
            cur_total += nums[i]

            while cur_total + total < 0:
                cur_total -= nums[s]
                s += 1
            cur_len = i - s
            if cur_len > best_len:
                best_len = cur_len
                best_range = [s + 1, i + 1]

        if best_range[0] != -float('inf'):
            print(*best_range)
        else:
            print(-1)

solve()
