# https://codeforces.com/group/b5GBy1CJ0d/contest/368852/problem/A

t = int(input())
for _ in range(t):
    s = input()
    ans = set()
    cur = [' ', 0]
    for c in s + ' ':
        if c != cur[0]:
            if cur[1] % 2:
                ans.add(cur[0])
            cur = [c, 1]
        else:
            cur[1] += 1

    print(''.join(sorted(ans)))
    
