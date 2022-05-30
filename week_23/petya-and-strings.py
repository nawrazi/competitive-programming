# https://codeforces.com/gym/383731/problem/A

s1 = input().lower()
s2 = input().lower()

if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)