# https://codeforces.com/gym/392476/problem/A

t = int(input())
for _ in range(t):
    num = input()
    if int(num[-1]) % 2 == 0:
        print(0)
    elif int(num[0]) %2 == 0:
        print(1)
    else:
        found = False
        for n in num:
            if int(n) % 2 == 0:
                print(2)
                found = True
                break
        if not found:
            print(-1)
            