# https://codeforces.com/gym/407909/problem/B

for _ in range(int(input())):
    input()
    arr = [int(i) for i in input().split()]
    ans = (1 << 32) - 1
    for a in arr:
        ans &= a
    print(ans)
    
