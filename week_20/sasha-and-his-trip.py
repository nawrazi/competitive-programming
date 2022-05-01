def solve(cities, tank):
    if tank > cities:
        print(cities - 1)
    else:
        print(tank - 1 + (cities - tank)*(cities - tank + 1) // 2)


cities, tank = [int(i) for i in input().split()]
solve(cities, tank)
