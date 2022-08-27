# https://codeforces.com/gym/396349/problem/B

from collections import Counter, defaultdict

t = int(input())
for _ in range(t):
    s = input()
    target = int(input())
    score = 0
    value = {}
    count = Counter(s)

    for c in s:
        cur = ord(c) - ord('a') + 1
        score += cur
        value[c] = cur

    values = sorted([(v, c, count[c]) for c, v in value.items()])
    rem = defaultdict(int)
    while values and score > target:
        val, c, cnt = values.pop()
        score -= val
        rem[c] += 1
        if cnt > 1:
            values.append([val, c, cnt - 1])

    final = ""
    for c in s:
        if rem[c] == 0:
            final += c
        else:
            rem[c] -= 1

    print(final)
