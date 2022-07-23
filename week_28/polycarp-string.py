t = int(input())
for _ in range(t):
    s = input()
    fam = set()
    days = 0
    for c in s:
        if c not in fam:
            fam.add(c)
        if len(fam) > 3:
            days += 1
            fam.clear()
            fam.add(c)
    print(days + int(bool(fam)))
    fam.clear()
