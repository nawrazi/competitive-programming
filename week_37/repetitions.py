# https://cses.fi/problemset/task/1069

s = input()
cur, count = s[0], 0
max_count = 0

for c in s + ' ':
    if c == cur:
        count += 1
    else:
        max_count = max(count, max_count)
        cur, count = c, 1

print(max_count)