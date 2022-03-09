# https://codeforces.com/problemset/problem/1629/A

def solve(ram_specs, my_ram):
    for input, output in ram_specs:
        if my_ram >= input:
            my_ram += output
    print(my_ram)

t = int(input())
for _ in range(t):
    n, my_ram = [int(i) for i in input().split()]
    inputs = [int(i) for i in input().split()]
    outputs = [int(i) for i in input().split()]
    ram_specs = sorted([(inputs[i], outputs[i]) for i in range(n)])

    solve(ram_specs, my_ram)
