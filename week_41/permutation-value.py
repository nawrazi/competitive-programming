# https://codeforces.com/contest/1743/problem/B

for _ in range(int(input())):
    print(' '.join(['1'] + [str(i + 3) for i in range(int(input()) - 2)] + ['2']))
    
