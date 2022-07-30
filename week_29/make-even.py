t = int(input())
for _ in range(t):
    num = input()
    if int(num[-1]) % 2 == 0:
        print(0)
        continue
    elif int(num[0]) %2 == 0:
        print(1)
        continue
    else:
        found = False
        for n in num:
            if int(n) % 2 == 0:
                print(2)
                found = True
                break
        if not found:
            print(-1)