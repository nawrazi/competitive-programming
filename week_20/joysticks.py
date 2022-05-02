# https://codeforces.com/gym/380193/problem/C

def solve(batteries):
    tbd, tbc = max(batteries), min(batteries)
    time = 0

    while tbd >= 1 and tbd + tbc > 2:
        if tbd <= 2:
            tbd, tbc = tbc, tbd

        tbd -= 2
        tbc += 1
        time += 1

    print(time)


batteries = [int(i) for i in input().split()]
solve(batteries)
