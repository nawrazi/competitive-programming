# https://codeforces.com/gym/408379/problem/A

for _ in range(int(input())):
    l, r, a = [int(i) for i in input().split()]
    best = ((r + 1) // a) * a
    if best <= l:
        print((r // a) + (r % a))
    else:
        best -= 1
        print((best // a) + (best % a))
        
