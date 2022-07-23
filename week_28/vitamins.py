vals = {
    'A': float('inf'),
    'B': float('inf'),
    'C': float('inf'),
    'AB': float('inf'),
    'AC': float('inf'),
    'BC': float('inf'),
    'ABC': float('inf'),
}

n = int(input())
for _ in range(n):
    price, vit = input().split()
    key = ''.join(sorted(vit))
    vals[key] = min(vals[key], int(price))

poss = [
    vals['A'] + vals['B'] + vals['C'],
    vals['AB'] + vals['C'],
    vals['AC'] + vals['B'],
    vals['BC'] + vals['A'],
    vals['AB'] + vals['BC'],
    vals['AC'] + vals['BC'],
    vals['AB'] + vals['AC'],
    vals['ABC'],
]

ans = min(poss)
print(ans if ans != float('inf') else -1)
