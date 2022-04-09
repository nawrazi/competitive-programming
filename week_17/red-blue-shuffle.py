def solve(red, blue):
    blue_chance, red_chance = 0, 0
    for i in range(size):
        if red[i] > blue[i]:
            red_chance += 1

        if blue[i] > red[i]:
            blue_chance += 1

    if blue_chance > red_chance:
        print('BLUE')
    elif blue_chance < red_chance:
        print('RED')
    else:
        print('EQUAL')


t = int(input())
for _ in range(t):
    size = int(input())
    red = [int(i) for i in list(input())]
    blue = [int(i) for i in list(input())]
    solve(red, blue)
